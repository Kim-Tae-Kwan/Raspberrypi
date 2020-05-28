import RPi.GPIO as GPIO
import time

RED = 21
GREEN = 20
BLUE = 16

def Rlight():
    GPIO.output(RED,True)
    GPIO.output(GREEN,False)
    GPIO.output(BLUE,False)

def Glight():
    GPIO.output(RED,False)
    GPIO.output(GREEN,True)
    GPIO.output(BLUE,False)

def Blight():
    GPIO.output(RED,False)
    GPIO.output(GREEN,False)
    GPIO.output(BLUE,True)


GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

try:
    while(True): #loop
        a=int(input('색깔 입력 : '))

        if(a==1):
            Rlight()
        elif(a==2):
            Glight()
        elif(a==3):
            Blight()
        elif(a==4):
            Rlight()
            time.sleep(0.5)
            Glight()
            time.sleep(0.5)
            Blight()
            time.sleep(0.5)
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()

