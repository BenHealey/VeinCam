# VeinCam Camera stream emulation script
# Idea from https://blog.miguelgrinberg.com/post/video-streaming-with-flask

# Imports Libraries
import os
import time
import numpy as np
import cv2
from camera_base import BaseCamera
from flask import Flask

# Obtains name of current Flask Module
app = Flask(__name__)


class Camera(BaseCamera):
    cv_images = [cv2.imread(os.path.join(app.static_folder, 'images/testhires/test_image') + suffix + '.jpeg', 0)
                 for suffix in ['1', '2', '3', '4', '5']]

    # Initialises Settings
    settings = {}

    # Sets Sizes For Image Manipulation and Initialises ROI Map
    img_height, img_width = 1920, 1080
    crop_height, crop_width = 1000, 1000
    roi_large_height, roi_large_width = 600, 600
    roi_small_height, roi_small_width = 400, 400
    roi_map = {}

    # Defines Crop Ranges from Centre of Image
    crop_height_start = int((img_height / 2) - (crop_height / 2))
    crop_height_end = crop_height_start + crop_height
    crop_width_start = int((img_width / 2) - (crop_width / 2))
    crop_width_end = crop_width_start + crop_width

    # Defines Large ROI Range from Centre of Cropped Image
    roil_height_start = int((crop_height / 2) - (roi_large_height / 2))
    roil_height_end = roil_height_start + roi_large_height
    roil_width_start = int((crop_width / 2) - (roi_large_width / 2))
    roil_width_end = roil_width_start + roi_large_width
    roi_map["Large"] = {"roi_height_start": roil_height_start, "roi_height_end": roil_height_end,
                        "roi_width_start": roil_width_start, "roi_width_end": roil_width_end}

    # -- ROI range small
    rois_height_start = int((crop_height / 2) - (roi_small_height / 2))
    rois_height_end = rois_height_start + roi_small_height
    rois_width_start = int((crop_width / 2) - (roi_small_width / 2))
    rois_width_end = rois_width_start + roi_small_width
    roi_map["Small"] = {"roi_height_start": rois_height_start, "roi_height_end": rois_height_end,
                        "roi_width_start": rois_width_start, "roi_width_end": rois_width_end}

    @staticmethod
    def update_settings(settings):
        Camera.settings = settings

    @staticmethod
    def close():
        pass

    @staticmethod
    def frames():
        roi_setting = "Off"
        frame_rate = 1
        period = round(1/frame_rate, 4)
        index = 0
        while True:
            # Runs at Frame Rate
            time.sleep(period)

            if bool(Camera.settings):
                try:
                    # print(Camera.settings["cam_contrast"])
                    roi_setting = Camera.settings["roi"]
                except KeyError:
                    print('Camera has no ROI setting')

            # Acquires Image
            image = Camera.cv_images[index]

            # Updates Image Index
            if index == 4:
                index = 0
            else:
                index += 1

            # Crops the Image and Creates a Copy
            image = image[Camera.crop_height_start: Camera.crop_height_end,
                          Camera.crop_width_start: Camera.crop_width_end]
            img_final = image.copy()

            # Applies Histogram Equalisation to ROI
            if roi_setting in ("Large", "Small"):
                roi_ranges = Camera.roi_map[roi_setting]
                roi = image[roi_ranges["roi_height_start"]: roi_ranges["roi_height_end"],
                            roi_ranges["roi_width_start"]: roi_ranges["roi_width_end"]]

                # OpenCV Histogram Equalisation
                hist_eq = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(5, 5))
                roi = hist_eq.apply(roi)

                # Overwrite the ROI into a composite final - must use copy of image
                img_final[roi_ranges["roi_height_start"]: roi_ranges["roi_height_end"],
                          roi_ranges["roi_width_start"]: roi_ranges["roi_width_end"]] = roi

            # Yields Output Image
            yield cv2.imencode('.jpg', img_final)[1].tobytes()
