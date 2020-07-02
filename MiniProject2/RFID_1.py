#RFID 작동 보기
import serial

port='/dev/ttyACM0'
brate = 9600 
cmd = 'temp'

ser= serial.Serial(port,baudrate=brate,timeout=None)
print(ser.name)

while True:
    try:

        if ser.in_waiting !=0:
            content = ser.readline()
            print(content)

    except KeyboardInterrupt:
        GPIO.cleanup()


            
        