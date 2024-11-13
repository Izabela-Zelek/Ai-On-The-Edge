import paho.mqtt.client as mqtt

# Initialize MQTT client
mqtt_client = mqtt.Client()
broker_address = "broker_ip_address"  # Replace with your MQTT broker's IP
mqtt_client.connect(broker_address)

def publish_context(context_message):
    mqtt_client.publish("context/awareness", context_message)
    print(f"Published context: {context_message}")
    
def check_comfort_level():
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    temp = round(temp, 1)
    humidity = round(humidity, 1)

    is_temp_comfortable = TEMP_LOWER <= temp <= TEMP_UPPER
    is_humidity_comfortable = HUMIDITY_LOWER <= humidity <= HUMIDITY_UPPER
    if is_temp_comfortable and is_humidity_comfortable:
        context_message = "Comfortable"
        sense.show_message(context_message, text_colour=[0, 255, 0])
        print("Environment is comfortable.")
    else:
        context_message = "Uncomfortable"
        sense.show_message(context_message, text_colour=[255, 0, 0])
        print("Environment is uncomfortable.")
    publish_context(context_message)
    print(f"Temperature: {temp}°C, Humidity: {humidity}%")