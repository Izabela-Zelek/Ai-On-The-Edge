import paho.mqtt.client as mqtt
import json

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
    if reason_code == 0:
        print("Connected to broker (MQTTv5)")
        client.subscribe("sensors/environment")
    else:
        print("Connection failed with reason code ", reason_code)
    
def on_message(client, userdata, msg):
    """
    The callback for when a PUBLISH message is received from the broker
    Parameters:
    -client: the client instance
    -userdata: the private user dataas set in Client() or userdata_set()
    -msg: an instance of MQTTMessage, which contains topic, payload, qos, retain
    """
    data_in = json.loads(msg.payload.decode())
    print("Received data:", data_in)
    
client = mqtt.Client(protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message

broker_address = "localhost"
client.connect(broker_address)

client.loop_forever()