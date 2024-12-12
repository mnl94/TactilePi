#!/usr/bin/python3

from picamera2 import Picamera2
import time
import cv2
import numpy as np
import os
from datetime import datetime

# File for captured image
filename = './scenes/photo.png'

# Camera settings
cam_width = 640
cam_height = 360
scale_ratio = 0.5

# Camera resolution height must be dividable by 16, and width by 32
cam_width = int((cam_width + 31) / 32) * 32
cam_height = int((cam_height + 15) / 16) * 16
print(f"Used camera resolution: {cam_width} x {cam_height}")

# Buffer for captured image settings
img_width = int(cam_width * scale_ratio)
img_height = int(cam_height * scale_ratio)
print(f"Scaled image resolution: {img_width} x {img_height}")

# Initialize the left camera
caml = Picamera2(1)
camr = Picamera2(0)
cam_config = caml.create_video_configuration(main={"size": (cam_width,cam_height)})
caml.configure(cam_config)
camr.configure(cam_config)
caml.start()
camr.start()

t2 = datetime.now()
counter = 0
avgtime = 0

# Capture frames from the camera
while True:
    frame_left = caml.capture_array()
    frame_right = camr.capture_array()

    frame_combined = np.concatenate((frame_left,frame_right), axis=1)
    #frame_combined = cv2.resize(frame_combined, (img_width, img_height))

    # Convert RGB to BGR
    frame_combined = cv2.cvtColor(frame_combined, cv2.COLOR_RGB2BGR)

    counter += 1
    t1 = datetime.now()
    timediff = t1 - t2
    avgtime += timediff.total_seconds()
    cv2.imshow("pair", frame_combined)
    key = cv2.waitKey(1) & 0xFF
    t2 = datetime.now()

    # if the `q` key was pressed, break from the loop and save last image
    if key == ord("q"):
        avgtime /= counter
        print(f"Average time between frames: {avgtime}")
        print(f"Average FPS: {1 / avgtime}")
        if not os.path.isdir("./scenes"):
            os.makedirs("./scenes")
        cv2.imwrite(filename, frame_combined)
        break

cv2.destroyAllWindows()
caml.stop()

