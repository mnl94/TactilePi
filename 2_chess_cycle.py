import os
import time
from datetime import datetime
import picamera2
from picamera2 import Picamera2
import cv2
import numpy as np

# Image capture settings
scale_ratio = 1.0
cam_width = 640
cam_height = 360

# Camera resolution height must be dividable by 16, and width by 32
cam_width = int((cam_width+31)/32)*32
cam_height = int((cam_height+15)/16)*16
print ("Used camera resolution: "+str(cam_width)+" x "+str(cam_height))

# Photo session settings
total_photos = 30             # Number of images to take
countdown = 5                 # Interval for count-down timer, seconds
font=cv2.FONT_HERSHEY_SIMPLEX # Cowntdown timer font

# Initialize the cameras
caml = Picamera2(1)
camr = Picamera2(0)
cam_config = caml.create_video_configuration(main={"size":(cam_width,cam_height)})
caml.configure(cam_config)
camr.configure(cam_config)
caml.start()
camr.start()

# Buffer for captured image settings
img_width = int(cam_width * scale_ratio)
img_height = int(cam_height * scale_ratio)


# Lets start taking photos! 
counter = 0
t2 = datetime.now()
print ("Starting photo sequence")
while True:
    frame_left = caml.capture_array()
    frame_right = camr.capture_array()
    frame = np.concatenate((frame_left,frame_right),axis=1)
    # Convert RGB to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    t1 = datetime.now()
    cntdwn_timer = countdown - int ((t1-t2).total_seconds())
    # If cowntdown is zero - let's record next image
    if cntdwn_timer == -1:
      counter += 1
      filename = './scenes/scene_'+str(img_width*2)+'x'+str(img_height)+'_'+\
                  str(counter) + '.png'
      cv2.imwrite(filename, frame)
      print (' ['+str(counter)+' of '+str(total_photos)+'] '+filename)
      t2 = datetime.now()
      time.sleep(1)
      cntdwn_timer = 0      # To avoid "-1" timer display
      next
    # Draw countdown counter, seconds
    cv2.putText(frame, str(cntdwn_timer), (50,50), font, 2.0, (0,0,255),4, cv2.LINE_AA)
    cv2.imshow("pair", frame)
    key = cv2.waitKey(1) & 0xFF

    # Press 'Q' key to quit, or wait till all photos are taken
    if (key == ord("q")) | (counter == total_photos):
      break


print ("Photo sequence finished")

