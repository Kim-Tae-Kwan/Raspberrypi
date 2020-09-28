import paho.mqtt.client as mqtt
import time 
import smbus
import RPi.GPIO as GPIO


AVR_2_ADDRESS = 0x015

I2Cbus = smbus.SMBus(1) 
  
SlaveAddress = AVR_2_ADDRESS

def ConvertStringToBytes(src): 
  converted = [] 
  for b in src: 
    converted.append(ord(b))
  # Appending CR code
    #converted.append(13)
  return converted

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
        flag = 0 
    else:
        print("Bad connection Returned code=", rc)

def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))
    if(str(msg.payload.decode("utf-8"))=='1'):
        SlaveAddress = AVR_2_ADDRESS
        out_data = 'q'
        bytes_ch = ConvertStringToBytes(out_data)
        for i in range(len(bytes_ch)):
    # 문자(Byte)를 Slave에 전송 한다.
    # cmd = 0xa0 : 이 코드를 Slave에서 문자 수신 명령으로 해석 한다.
            I2Cbus.write_byte_data(SlaveAddress, 0xa0, ord(out_data))
            time.sleep(0.01)

    # 수신한 문자열을 저장할 변수
            out_str = ''
    elif(str(msg.payload.decode("utf-8"))=='2'):
        SlaveAddress = AVR_2_ADDRESS
        out_data = 'z'
        bytes_ch = ConvertStringToBytes(out_data)
        for i in range(len(bytes_ch)):
    # 문자(Byte)를 Slave에 전송 한다.
    # cmd = 0xa0 : 이 코드를 Slave에서 문자 수신 명령으로 해석 한다.
            I2Cbus.write_byte_data(SlaveAddress, 0xa0, ord(out_data))
            time.sleep(0.01)

    # 수신한 문자열을 저장할 변수
            out_str = ''
    elif(str(msg.payload.decode("utf-8"))=='3'):
        SlaveAddress = AVR_2_ADDRESS
        out_data = 'w'
        bytes_ch = ConvertStringToBytes(out_data)
        for i in range(len(bytes_ch)):
    # 문자(Byte)를 Slave에 전송 한다.
    # cmd = 0xa0 : 이 코드를 Slave에서 문자 수신 명령으로 해석 한다.
            I2Cbus.write_byte_data(SlaveAddress, 0xa0, ord(out_data))
            time.sleep(0.01)

    # 수신한 문자열을 저장할 변수
            out_str = ''
    elif(str(msg.payload.decode("utf-8"))=='4'):
        SlaveAddress = AVR_2_ADDRESS
        out_data = 'x'
        bytes_ch = ConvertStringToBytes(out_data)
        for i in range(len(bytes_ch)):
    # 문자(Byte)를 Slave에 전송 한다.
    # cmd = 0xa0 : 이 코드를 Slave에서 문자 수신 명령으로 해석 한다.
            I2Cbus.write_byte_data(SlaveAddress, 0xa0, ord(out_data))
            time.sleep(0.01)

    # 수신한 문자열을 저장할 변수
            out_str = ''
    elif(str(msg.payload.decode("utf-8"))=='5'):
        SlaveAddress = AVR_2_ADDRESS
        out_data = 'e'
        bytes_ch = ConvertStringToBytes(out_data)
        for i in range(len(bytes_ch)):
    # 문자(Byte)를 Slave에 전송 한다.
    # cmd = 0xa0 : 이 코드를 Slave에서 문자 수신 명령으로 해석 한다.
            I2Cbus.write_byte_data(SlaveAddress, 0xa0, ord(out_data))
            time.sleep(0.01)

    # 수신한 문자열을 저장할 변수
            out_str = ''
    elif(str(msg.payload.decode("utf-8"))=='6'):
        SlaveAddress = AVR_2_ADDRESS
        out_data = 'c'
        bytes_ch = ConvertStringToBytes(out_data)
        for i in range(len(bytes_ch)):
    # 문자(Byte)를 Slave에 전송 한다.
    # cmd = 0xa0 : 이 코드를 Slave에서 문자 수신 명령으로 해석 한다.
            I2Cbus.write_byte_data(SlaveAddress, 0xa0, ord(out_data))
            time.sleep(0.01)

    # 수신한 문자열을 저장할 변수
            out_str = ''
try:
    # 새로운 클라이언트 생성
    client = mqtt.Client()
    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('210.119.12.60',1883)
    # common topic 으로 메세지 발행
    client.subscribe('home/device/led/', 1)
    client.loop_forever()
finally:
    GPIO.cleanup()


