import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import csv


TEMP_THRESHOLD = 25.0 # degrees Celsius
HUMIDITY_THRESHOLD = 30.0 # percentage
MOTION_THRESHOLD = 1.0 # acceleration threshold
TEMP_OFFSET = -10.0  # Adjust based on calibration
TEMP_LOWER = 20.0
TEMP_UPPER = 25.0
HUMIDITY_LOWER = 25.0
HUMIDITY_UPPER = 60.0

sense = SenseHat()

# Initialize MQTT client
mqtt_client = mqtt.Client()
broker_address = "localhost"  # Replace with your MQTT broker's IP
mqtt_client.connect(broker_address)

def calculate_average_conditions():
    temps = []
    humidities = []
    try:
        with open("sensor_data.csv", "r") as data_file:
            reader = csv.reader(data_file)
            for row in reader:
                if len(row) == 3:
                    temps.append(float(row[1]))
                    humidities.append(float(row[2]))
        # Consider only the last 12 entries (assuming 5-minute intervals for the last hour)
        temps = temps[-12:]
        humidities = humidities[-12:]
        avg_temp = sum(temps) / len(temps) if temps else None
        avg_humidity = sum(humidities) / len(humidities) if humidities else None
        return avg_temp, avg_humidity
    except FileNotFoundError:
        print("No historical data available.")
        return None, None


def log_sensor_data(temp, humidity):
    with open("sensor_data.csv", "a", newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), temp, humidity])
        
def publish_context(context_message):
    mqtt_client.publish("context/awareness", context_message)
    print(f"Published context: {context_message}")
    
def check_comfort_level():
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    temp = round(temp, 1)
    humidity = round(humidity, 1)

    log_sensor_data(temp, humidity)
    avg_temp, avg_humidity = calculate_average_conditions()

    if avg_temp and avg_humidity:
        print(f"Average Temperature: {avg_temp:.1f}°C, Average Humidity: {avg_humidity:.1f}%")
        # Compare current readings to averages
        if temp > avg_temp + 2:
            sense.show_message("Getting warmer", text_colour=[255, 165, 0])  # Orange text
        elif temp < avg_temp - 2:
            sense.show_message("Getting cooler", text_colour=[0, 165, 255])  # Light blue text
    
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
    
def main():
    try:
        while True:
            check_comfort_level()
            time.sleep(5)  # Wait for 5 seconds before next check
    except KeyboardInterrupt:
        sense.clear()
        print("Program terminated.")
        
if __name__ == "__main__":
    main()