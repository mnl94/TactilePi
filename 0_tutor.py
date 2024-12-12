#!/usr/bin/python3
from picamera2 import Picamera2

caml = Picamera2(0)
camr = Picamera2(1)

caml.start()
camr.start()

caml.capture_file("caml.jpg")
camr.capture_file("camr.jpg")

caml.stop()
camr.stop()
