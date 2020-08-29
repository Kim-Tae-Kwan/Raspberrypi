import picamera
import time

cam = picamera.PiCamera()
cam.start_preview()
time.sleep(10)
cam.stop_preview()
cam.capture('./dataset/capture2.jpg')
