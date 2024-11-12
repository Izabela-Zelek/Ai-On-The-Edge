import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import json

sense = SenseHat()
client = mqtt.Client()
broker_address = "localhost" # Use appropriate IP if on different device
client.connect(broker_address)

try:
    while True:
        temp = sense.get_temperature()
        data = {"temperature": temp}
        data_out = json.dumps(data)
        client.publish("sensors/temperature", data_out)
        print("Published temperature:", data_out)
        time.sleep(5)
except KeyboardInterrupt:
    print("Temperature publisher stopped.")
