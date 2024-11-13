import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to broker.")
    client.subscribe("context/awareness")

def on_message(client, userdata, msg):
    context_message = msg.payload.decode()
    print(f"Received context: {context_message}")
    # Take action based on context
    if context_message == "Uncomfortable":
        print("Taking action due to uncomfortable conditions.")        
        
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
broker_address = "localhost"  # Replace with your MQTT broker's IP
mqtt_client.connect(broker_address)
mqtt_client.loop_forever()