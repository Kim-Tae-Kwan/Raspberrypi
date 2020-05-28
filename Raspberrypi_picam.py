import picamera
import time


# 카메라 출력 확인
# with picamera.PiCamera() as camera:
#     camera.start_preview()
#     time.sleep(1000)
#     camera.stop_preview()

# 영상 녹화 프로그램
# with picamera.PiCamera() as camera:
#     camera.resolution = (640,480)
#     camera.start_preview()
#     camera.start_recording('kim.h264')
#     camera.wait_recording(60)
#     camera.stop_recording()
#     camera.stop_preview()

# 영상 캡쳐 프로그램
# with picamera.PiCamera() as camera:
#     camera.resolution = (640,480)
#     camera.start_preview()
#     camera.exposure_compensation=2
#     camera.exposure_mode = 'spotlight'
#     camera.meter_mode = 'matrix'
#     camera.image_effect = 'gpen'

#     time.sleep(2)
#     camera.exif_tags['IFD0.Artist'] = 'Kim'
#     camera.exif_tags['IFD0.Copyright'] = 'Copyleft Kim'
#     camera.capture('kim.jpg')
#     camera.stop_preview()
