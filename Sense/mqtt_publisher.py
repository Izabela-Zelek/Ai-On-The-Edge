import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import json

sense = SenseHat()
client = mqtt.Client()

broker_address = "localhost"
client.connect(broker_address)

try:
    while True:
        temp = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        
        #Creating data payload
        data = {
            "Temperature": temp,
            "Humidity": humidity,
            "Pressure": pressure
            }
        data_out = json.dumps(data)
        
        client.publish("sensors/environment", data_out)
        print("Published data:", data_out)
        time.sleep(5)
        
except KeyboardInterrupt:
    print("Publisher stopped")