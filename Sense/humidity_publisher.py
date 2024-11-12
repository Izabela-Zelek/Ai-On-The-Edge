import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import json

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection. Reconnecting...")
    else:
        print("Disconnected from broker")
        
sense = SenseHat()
client = mqtt.Client()
broker_address = "localhost" 
client.connect(broker_address)


try:
    while True:
        
        client.reconnect_delay_set(min_delay=1, max_delay=120)
        client.on_disconnect = on_disconnect
        humidity = sense.get_humidity()
        data = {"humidity": humidity}
        data_out = json.dumps(data)
        client.publish("sensors/humidity", data_out)
        print("Published humidity:", data_out)
        time.sleep(5)
except KeyboardInterrupt:
    print("Humidity publisher stopped.")
