import os
import re
import psutil
from flask import Flask, render_template, request, Response, json

#from camera_piopencv import Camera
#import pigpio as io

#TODO - delete from production
if os.name == 'nt':
    DEBUG = True
    baseurl='http://localhost:5000'
    from windev.emulated_camera import Camera
    import windev.emulated_pigpio as io
    print('Dev mode')
else:
    DEBUG = False
    baseurl='http://10.0.0.5:5000'
    from camera_piopencv import Camera # RPi camera module (requires picamera pckg)
    import pigpio as io
    print('Prod mode')

app = Flask(__name__)


'''Settings and Statistics Dictionary Functions'''
# Creates map to wifi setup file
wifi_file = os.path.join('etc','hostapd','hostapd.conf')

if DEBUG: #TODO delete from production
    wifi_file = os.path.join(app.root_path, 'hostapd.conf')


# Creates Setting Cache
settings_file = os.path.join(app.static_folder, 'json', 'settings.json')
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


def update_wifi_settings(attr,val):
    print("updating wifi")
    with open(wifi_file,'r') as f:
            in_file = f.read()
            f.close()

    if attr == 'wifi_pwd':
        out_file =  re.sub(r'wpa_passphrase=.*','wpa_passphrase='+val, in_file)

    if attr == 'wifi_ssid':
        out_file =  re.sub(r'ssid=.*','ssid='+val,in_file)

    with open(wifi_file,'w') as f:
            f.write(out_file)
            f.close()

'''Global Render Template'''
@app.route('/')
def index():
    pipin.write(4, 0) # Turn Ready LEDs OFF - user knows this already.
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
    [pipin.write(pin,0) for pin in LEDPinMap['Both']]


'''App Altering Functions'''
def alter_light_level(val):
    intval=int(val)
    if intval in (1, 2, 3):
        duty_cycle = 333333*intval  # Max = 1000000
        activeLEDs = LEDPinMap[settings_cache['light_wavelength']].intersection(LEDPinMap["Rail5V"])
        [pipin.hardware_PWM(pin, 750, duty_cycle) for pin in activeLEDs]

        if val != settings_cache['light_level']:
            update_settings_cache('light_level', val)
    else:
        all_led_off()


def alter_cam_setting(attr,val):

    if val in ["850nm", "Both", "940nm"]:
        all_led_off()
        alter_light_level(settings_cache['light_level'])
    elif attr == 'light_level':
        alter_light_level(request.form['value'])
    elif attr == 'camera_state':
        value = request.form['value'] == 'true'
        if value:
            alter_cam_setting('light_wavelength', settings_cache['light_wavelength'])
        else:
            all_led_off()
    elif attr in ['wifi_pwd','wifi_ssid']:
        update_wifi_settings(attr, val)
    else:
        pass
    
    update_settings_cache(attr, val)
    #TODO last line shouldn't run if above it failed.

        


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
    return json.dumps({'status':'Server shutting down...'})


'''Shutdown RPi Functions'''
def shutdownPi():
    from subprocess import call
    call("sudo nohup shutdown -h now", shell=True)
    return json.dumps({'status':'Server pi down...'})

'''Shutdown RPi Route'''
@app.route('/shutpi', methods=['POST'])
def shutpi():
    shutdownPi()
    return json.dumps({'status':'Pi shutting down...'})


'''Settings Allter Route'''
@app.route('/alter-config', methods=['POST'])
def alter_config():
    attribute = request.form['attribute']
    value = request.form['value']
    print('>attribute ', attribute, '| value ', value)
    alter_cam_setting(attribute, value)
    return json.dumps({'status':'OK'})


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
        # Turn Ready LED ON, Boot LED OFF, and Start Server
        pipin.write(4, 1) # Ready
        pipin.write(14, 0) # Boot
        all_led_off() # IR LEDs
        app.run(host='0.0.0.0', port='5000', debug=False, threaded=True)
        #TODO PORT https://www.raspberrypi.org/forums/viewtopic.php?t=33708
        # https://raspberrypi.stackexchange.com/questions/57777/making-a-raspberry-pi-3-accessible-w-o-configuration-via-wifi-and-static-ip-url
    except:
        # Turn Ready LEDs OFF - we are screwed.
        pipin.write(4, 0)
        