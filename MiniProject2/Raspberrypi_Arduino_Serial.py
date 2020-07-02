#라즈베리파이 아두이노 연결
import serial
import RPi.GPIO as GPIO

RED = 25; GREEN = 24; BLUE = 23
GPIO.setmode(GPIO.BCM)

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)


port='/dev/ttyACM0'
brate = 9600 
cmd = 'temp'

ser= serial.Serial(port,baudrate=brate,timeout=None)
print(ser.name)

while True:
    try:

        if ser.in_waiting !=0:
            content = ser.readline()
                  
            content = content.decode('utf-8').replace('\r\n','')
            
            vals = content.split(' ')

            if len(vals)<1:
                continue
            
            vals=int(vals[0])
            print(vals)
            GPIO.output(GREEN,vals)
            

        
            
            #GPIO.output(GREEN,vals)
             
            
            
            # if len(vals)<3:
            #     continue

            # print(vals)
            # if vals[0] == '0':
            #     GPIO.output(RED,GPIO.LOW)
            # elif vals[0]== '1023':
            #     GPIO.output(RED,GPIO.HIGH)
            
            # if vals[1] == '0':
            #     GPIO.output(GREEN,GPIO.LOW)
            # elif vals[1]== '1023':
            #     GPIO.output(GREEN,GPIO.HIGH)

            # if vals[2] == '1':
            #     GPIO.output(BLUE,GPIO.LOW)
            # elif vals[2]== '0':
            #     GPIO.output(BLUE,GPIO.HIGH)
            

    except KeyboardInterrupt:
        GPIO.cleanup()

            
        