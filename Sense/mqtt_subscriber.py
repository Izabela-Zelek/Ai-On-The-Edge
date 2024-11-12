import paho.mqtt.client as mqtt
import json
from sense_hat import SenseHat


def on_connect(client, userdata, flags, reason_code, properties):
    """
    The callback for when the client receives CONNACK response from the broker
    Parameters:
    -client: the client instance
    -userdata: the private user dataas set in Client() or userdata_set()
    -flags: response flags sent by broker
    -reason_code: the connection result(v5 feature)
    -properties: connection properties (v5 feature)
    """
    #if reason_code == 0:
        #print("Connected to broker (MQTTv5)")
        #client.subscribe("sensors/environment")
    #else:
        #print("Connection failed with reason code ", reason_code)
    if reason_code == 0:
        print("Connected to broker")
        # Subscribe to multiple topics with QoS levels
        client.subscribe([("sensors/temperature", 0), ("sensors/humidity", 0)])
    else:
        print("Connection failed with code", rc)
    
def on_message(client, userdata, msg):
    """
    The callback for when a PUBLISH message is received from the broker
    Parameters:
    -client: the client instance
    -userdata: the private user dataas set in Client() or userdata_set()
    -msg: an instance of MQTTMessage, which contains topic, payload, qos, retain
    """
    #data_in = json.loads(msg.payload.decode())
    #temperature = data_in["Temperature"]
    #print("Received temperature:", temperature)
    # Display temperature on the LED matrix
    #sense.show_message(f"{temperature:.1f}C", scroll_speed=0.075)
    topic = msg.topic
    data_in = json.loads(msg.payload.decode())
    if topic == "sensors/temperature":
        aggregated_data["temperature"] = data_in["temperature"]
    elif topic == "sensors/humidity":
        aggregated_data["humidity"] = data_in["humidity"]
    print("Aggregated data:", aggregated_data)
    
    # Check if both temperature and humidity data are available
    if "temperature" in aggregated_data and "humidity" in aggregated_data:
        temp = aggregated_data["temperature"]
        humidity = aggregated_data["humidity"]
        message = f"T:{temp:.1f}C H:{humidity:.1f}%"
        sense.show_message(message, scroll_speed=0.05)
        # Clear the aggregated data after displaying
        aggregated_data.clear()

sense = SenseHat()
aggregated_data = {}

client = mqtt.Client(protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message

broker_address = "localhost"
client.connect(broker_address)

client.loop_forever()