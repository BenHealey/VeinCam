import os

import psutil
from flask import Flask, render_template, request, Response, json

from camera_piopencv import Camera
import pigpio as io

app = Flask(__name__)


'''Settings and Statistics Dictionary Functions'''
# Creates Setting Cache
settings_file = os.path.join(app.static_folder, 'json/settings_custom.json')
settings_cache = json.load(open(settings_file))

# Creates System Statistics Cache
stats_cache = dict()


def update_settings_cache(attr, val):
    # Update both the in-memory dict and the SD card savefile
    settings_cache[attr] = val
    with open(settings_file, 'w') as sf:
        json.dump(settings_cache, sf, sort_keys=True, indent=4)
    return


def update_system_stats():
    stats_cache['cpu_usage'] = round(psutil.cpu_percent())
    stats_cache['ram_usage'] = round(psutil.virtual_memory().percent)
    try:
        ctemps = psutil.sensors_temperatures()
        stats_cache['cpu_temp'] = round(ctemps['cpu-thermal'][0][1])
    except AttributeError as error:
        # Output Expected AttributeErrors.
        print(error)
        stats_cache['cpu_temp'] = round(0.05)
    except Exception as exception:
        # Output Unexpected Exceptions.
        print(exception, False)
        stats_cache['cpu_temp'] = round(0.05)
    return


'''Global Render Template'''
@app.route('/')
def index():
    update_system_stats()
    return render_template('index.html',
                           config_data=settings_cache,
                           stats_data=stats_cache)


'''LED Declarations and Functions'''
LEDPinMap = {"850nm": {18},
             "940nm": {13},
             "Both": {13, 18},
             "Rail5V": {13, 18},
             }

pipin = io.pi()

def all_led_off():
    [pipin.write(pin, 0) for pin in LEDPinMap['Both']]


'''App Altering Functions'''
def alter_light_level(val):
    if val in (1, 2, 3):
        duty_cycle = 333333*val  # Max = 1000000
        activeLEDs5V = LEDPinMap[settings_cache['light_wavelength']].intersection(LEDPinMap["Rail5V"])
        [pipin.hardware_PWM(pin, 750, duty_cycle) for pin in activeLEDs5V]

        if val != settings_cache['light_level']:
            update_settings_cache('light_level', val)
    elif val == 0:
        all_led_off()
        if val != settings_cache['light_level']:
            update_settings_cache('light_level', val)
    else:
        pass


def alter_cam_setting(attr, val):
    if val in ["850nm", "Both", "940nm"]:
        all_led_off()
        update_settings_cache(attr, val)
        alter_light_level(settings_cache['light_level'])
    elif attr == 'light_level':
        value = int(request.form['value'])
        alter_light_level(value)
    elif attr == 'camera_state':
        update_settings_cache('cam_state', val)
        value = request.form['value'] == 'true'
        if value:
            alter_cam_setting('light_wavelength', settings_cache['light_wavelength'])
        else:
            all_led_off()
    else:
        update_settings_cache(attr, val)


'''Shutdown Server Functions'''
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


'''Shutdown Server Route'''
@app.route('/shutserver', methods=['POST'])
def shut_server():
    all_led_off()
    shutdown_server()
    return json.dumps({'status': 'Server shutting down...'})


'''Settings Allter Route'''
@app.route('/alter-config', methods=['POST'])
def alter_config():
    attribute = request.form['attribute']
    value = request.form['value']
    print('>attribute ', attribute, '| value ', value)
    alter_cam_setting(attribute, value)
    return json.dumps({'status': 'OK'})


'''Statistics Refresh Route'''
@app.route('/refresh-stats', methods=['POST'])
def refresh_stats():
    update_system_stats()
    print(stats_cache)
    current_stats = {**{'status':'OK'}, **stats_cache}
    return json.dumps(current_stats)


'''Main Camera Loop'''
def gen(camera):
    while settings_cache['cam_state']:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


'''Video Feed Route'''
@app.route('/video_feed', defaults={'increment': 0})
@app.route('/video_feed/<int:increment>/')
def video_feed(increment):
    global settings_cache
    camera = Camera(settings_cache)

    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


'''Main Script'''
if __name__ == '__main__':
    try:
        # Turn Ready LED ON and Start Server
        pipin.write(4, 1)
        all_led_off()
        app.run(host='0.0.0.0', port='8080', debug=False, threaded=True)
    finally:
        # Turn Ready LED OFF
        pipin.write(4, 0)
