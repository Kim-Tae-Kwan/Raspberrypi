import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

pin=18


try:
    while True:
        print('\nReading Temperature&Humidity')
        h,t=Adafruit_DHT.read_retry(sensor,pin)

        if h is not None and t is not None:
            print('Temp = {0:0.1f}C Humidity = {1:0.1f}%'.format(t,h))
        else:
            print('Read error')
        
        #time.sleep(0.5)
except KeyboardInterrupt:
    print('Terminated by Keyboard')
finally:
    print('End of program')