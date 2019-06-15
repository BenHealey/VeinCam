# Import Libraries
import io, os, time
import threading
from _thread import get_ident
import cv2
import numpy as np

from flask import Flask

app = Flask(__name__)

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
    pass


class Camera:
    """Obtains image, stores camera settings and performs image processing"""

    """An EMULATED camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self, settings_cache):
        self.settings = settings_cache

        # test images
        self.imgs = [open(os.path.normpath(os.path.join(os.getcwd(),'windev/testimages/')) + '/test_image' + suffix + '.jpeg', 'rb').read() 
            for suffix in ['1', '2', '3', '4', '5']]
        self.cvimgs = [cv2.imread(os.path.normpath(os.path.join(os.getcwd(),'windev/testimages/test_image')) + suffix + '.jpeg', 0) 
            for suffix in ['1', '2', '3', '4', '5']]


        # calculates crop and roi sizes
        self.res_height = 720
        self.res_width = 1280
        self.crop = self.crop_size(700, 450, self.res_height, self.res_width)
        self.roi = np.zeros([2, 4])
        self.roi[0] = self.crop_size(400, 250, 700, 450)
        self.roi[1] = self.crop_size(300, 200, 700, 450)
        self.roi = self.roi.astype(int)

        self.CLAHESet = np.zeros([2, 3])
        #Large settings - clip, horizontal, vertical.
        self.CLAHESet[0] = [5,6,6] #Large
        #Small settings - clip, horizontal, vertical.
        self.CLAHESet[1] = [10,6,8] #Large
        self.CLAHESet = self.CLAHESet.astype(int)

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
        # THIS CODE DOESN'T MATCH PROD CODE AT ALL
            time.sleep(1) 

            while True:
                time.sleep(0.5)

                img = self.cvimgs[int(time.time()) % 5]
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
            roi_img = img[self.roi[roi_index][0]: self.roi[roi_index][1], self.roi[roi_index][2]: self.roi[roi_index][3]]

            if self.settings["enhancement_method"] == "CLAHE":
                hist_eq = cv2.createCLAHE(
                    clipLimit=self.CLAHESet[roi_index][0], 
                    tileGridSize=(self.CLAHESet[roi_index][1],
                     self.CLAHESet[roi_index][2])
                    )
                roi_img = hist_eq.apply(roi_img)
            else:
                roi_img = cv2.bilateralFilter(roi_img,5,10,10)
                roi_img = cv2.equalizeHist(roi_img)
            
            """ Deprecated
            if (self.settings["color"] == 'On') & (self.settings["img_format"] == 'MJPEG'):
                lab = cv2.cvtColor(roi_img, cv2.COLOR_BGR2LAB)
                lab_split = cv2.split(lab)
                lab_split[0] = hist_eq.apply(lab_split[0])
                lab = cv2.merge(lab_split)
                roi_img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
            else:
                roi_img = hist_eq.apply(roi_img)

            """

            self.img_final[self.roi[roi_index][0]: self.roi[roi_index][1],
                           self.roi[roi_index][2]: self.roi[roi_index][3]] = roi_img