# Import Libraries
import io
import threading
import time
from _thread import get_ident

import cv2
import numpy as np
import picamera


class CameraEvent:
    """The Event class which signals main script when a new camera frame is available"""
    def __init__(self):
        self.events = {}

    def wait(self):
        ident = get_ident()
        if ident not in self.events:
            self.events[ident] = [threading.Event(), time.time()]
        return self.events[ident][0].wait()

    def set(self):
        now = time.time()
        remove = None
        for ident, event in self.events.items():
            if not event[0].isSet():
                event[0].set()
                event[1] = now
            else:
                if now - event[1] > 1:
                    remove = ident
        if remove:
            del self.events[remove]

    def clear(self):
        self.events[get_ident()][0].clear()


class StreamOutput:
    """Defines how the MJPEG stream writes to the buffer and splits each frame"""
    def __init__(self):
        self.frame = None
        self.stream = io.BytesIO()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.stream.seek(0)
            self.frame = self.stream.getvalue()
            self.stream.truncate()
            self.stream.seek(0)
        return self.stream.write(buf)


class Camera:
    """Obtains image, stores camera settings and performs image processing"""
    def __init__(self, settings_cache):
        self.settings = settings_cache

        # calculates crop and roi sizes
        self.res_height = 720
        self.res_width = 1280
        self.crop = self.crop_size(700, 450, self.res_height, self.res_width)
        self.roi = np.zeros([2, 4])
        self.roi[0] = self.crop_size(400, 250, 700, 450)
        self.roi[1] = self.crop_size(300, 200, 700, 450)
        self.roi = self.roi.astype(int)

        # starts camera thread and initiates event class
        self.thread = threading.Thread(target=self._thread)
        self.thread.start()
        self.event = CameraEvent()

    @staticmethod
    def crop_size(h, w, rh, rw):
        crop_points = []
        crop_points.append(int((rh / 2) - (h / 2)))
        crop_points.append(crop_points[0] + h)
        crop_points.append(int((rw / 2) - (w / 2)))
        crop_points.append(crop_points[2] + w)
        return np.array(crop_points)

    def update_settings(self):
        #print("Slf Sets UpDdtd - camera_state: %s" % self.settings["camera_state"])

        try:
            self.roi_setting = self.settings["enhancement_roi"]
            if int(self.pi_camera.contrast) != int(self.settings["cam_contrast"]):
                self.pi_camera.contrast = int(self.settings["cam_contrast"])
        except KeyError:
            print('No setting of that name currently in json file')

    def get_frame(self):
        self.event.wait()
        self.event.clear()
        return self.frame

    def _thread(self):
        print('Starting Camera Thread')
        frames_iterator = self.frames(self.settings["img_format"])
        for frame in frames_iterator:
            self.frame = frame
            self.event.set()
            if bool(self.settings):
                if self.settings["camera_state"] == 'false':
                    print('Stopping Camera Thread')
                    break

    def frames(self, img_format):
        with picamera.PiCamera(resolution=(self.res_width, self.res_height)) as self.pi_camera:
            time.sleep(1) 
            self.pi_camera.rotation = 180
            if img_format == "MJPEG":
                output = StreamOutput()
                self.pi_camera.start_recording(output, format='mjpeg')
                try:
                    while True:
                        try:
                            # if statements used to suppress initial OpenCV warnings
                            if output.frame is not None:
                                string_array = np.fromstring(output.frame, np.uint8)
                            if np.shape(string_array)[0] > 0:
                                if (self.settings["color"] == 'On') & (self.settings["img_format"] == 'MJPEG'):
                                    img = cv2.imdecode(string_array, cv2.IMREAD_COLOR)
                                else:
                                    img = cv2.imdecode(string_array, cv2.IMREAD_GRAYSCALE)
                            self.update_settings()
                            self.image_processing(img)
                            yield cv2.imencode('.jpg', self.img_final)[1].tobytes()
                        except GeneratorExit:
                            return
                        except UnboundLocalError:
                            pass
                        except cv2.error:
                            pass
                finally:
                    self.pi_camera.stop_recording()
            elif img_format == "YUV":
                raw_capture = np.empty(int(self.res_height * self.res_height * 1.5), dtype=np.uint8)
                for frame in self.pi_camera.capture_continous(raw_capture, format="yuv"):
                    img = raw_capture[:self.res_height*self.res_width].reshape((self.res_height, self.res_width))
                    self.update_settings()
                    self.image_processing(img)
                    yield cv2.imencode('.jpg', self.img_final)[1].tobytes()

    def image_processing(self, img):
        img = img[self.crop[0]:self.crop[1], self.crop[2]:self.crop[3]]
        self.img_final = img.copy()

        if self.roi_setting == "Large":
            roi_index = 0
        elif self.roi_setting == "Small":
            roi_index = 1

        if self.roi_setting in ("Large", "Small"):
            roi_img = img[self.roi[roi_index][0]: self.roi[roi_index][1],
                          self.roi[roi_index][2]: self.roi[roi_index][3]]

            if self.settings["enhancement_method"] == "CLAHE":
                hist_eq = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(6, 6))
                roi_img = hist_eq.apply(roi_img)
            else:
                roi_img = cv2.equalizeHist(roi_img)

            self.img_final[self.roi[roi_index][0]: self.roi[roi_index][1],
                           self.roi[roi_index][2]: self.roi[roi_index][3]] = roi_img
                           