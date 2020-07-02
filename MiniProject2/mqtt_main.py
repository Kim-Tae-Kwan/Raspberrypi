import paho.mqtt.client as mqtt
import Adafruit_DHT as dht
import json
import time
import datetime as dt
import uuid

from collections import OrderedDict

sensor = dht.DHT11
pin = 4
count = 0

try:
    dev_id = "TKKim"
    broker_add = "210.119.12.52"
    client2 = mqtt.Client(dev_id)
    client2.connect(broker_add)

    while True:
        count+=1
        currtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%s.%f')

        h,t = dht.read_retry(sensor,pin)

        raw_data = OrderedDict()
        raw_data["dev_id"] = dev_id
        raw_data["time"] = currtime
        raw_data["temp"] = "{0:0.1f}".format(t)
        raw_data["humi"] = "{0:0.1f}".format(h)

        pub_data = json.dumps(raw_data,ensure_ascii=False,indent="\t")

        print(dev_id,pub_data)
        
        client2.publish("home/device/data/",pub_data)
        time.sleep(5)

except Exception as ex:
    print('Error raised',ex)


