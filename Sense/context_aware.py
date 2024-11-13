from sense_hat import SenseHat
import time

sense = SenseHat()

TEMP_THRESHOLD = 25.0 # degrees Celsius
HUMIDITY_THRESHOLD = 30.0 # percentage
MOTION_THRESHOLD = 1.0 # acceleration threshold
TEMP_OFFSET = -10.0  # Adjust based on calibration
TEMP_LOWER = 20.0
TEMP_UPPER = 25.0
HUMIDITY_LOWER = 25.0
HUMIDITY_UPPER = 60.0

def check_temperature():
    temp = sense.get_temperature()
    temp = round(temp, 1)

    if temp > 28.0 + TEMP_OFFSET:
        sense.show_message("Warning: Hot!", text_colour=[255, 0, 0])
        # Log warning to a file
        with open("warnings.log", "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - High temperature: {temp}°C\n")
        print("Warning logged.")
    elif temp > TEMP_THRESHOLD + TEMP_OFFSET:
        sense.show_message("Hot!", text_colour=[255, 0, 0])
        print("Temperature Alert: Hot!")
    else:
        print("Temperature is normal.")
    print(f"Current Temperature: {temp}°C")
    
def check_humidity():
    humidity = sense.get_humidity()
    humidity = round(humidity, 1)  # Round to one decimal place

    if humidity < HUMIDITY_THRESHOLD:
        sense.show_message("Dry", text_colour=[0, 0, 255])  # Blue text
        print("Humidity Alert: Dry!")
    else:
        print("Humidity is normal.")
    print(f"Current Humidity: {humidity}%")
    
def check_motion():
    acceleration = sense.get_accelerometer_raw()
    x = abs(acceleration['x'])
    y = abs(acceleration['y'])
    z = abs(acceleration['z'])

    total_acceleration = x + y + z
    if total_acceleration > MOTION_THRESHOLD:
        # Display a flashing pattern
        for _ in range(3):
            sense.clear([255, 255, 0])  # Yellow color
            time.sleep(0.2)
            sense.clear()
            time.sleep(0.2)
        print("Motion detected with dynamic pattern!")
    else:
        print("No significant motion.")
        
def check_comfort_level():
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    temp = round(temp, 1)
    humidity = round(humidity, 1)

    is_temp_comfortable = TEMP_LOWER <= (temp + TEMP_OFFSET )<= TEMP_UPPER 
    is_humidity_comfortable = HUMIDITY_LOWER <= humidity <= HUMIDITY_UPPER
    if is_temp_comfortable and is_humidity_comfortable:
        sense.show_message("Comfortable", text_colour=[0, 255, 0])  # Green text
        print("Environment is comfortable.")
    else:
        message = "Uncomfortable"
        if not is_temp_comfortable:
            message += " Temp"
        if not is_humidity_comfortable:
            message += " Humidity"
        sense.show_message(message, text_colour=[255, 0, 0])  # Red text
        print("Environment is uncomfortable.")
    print(f"Temperature: {temp}°C, Humidity: {humidity}%")
    
def main():
    try:
        while True:
            #check_temperature()
            #check_humidity()
            check_comfort_level()
            check_motion()
            time.sleep(5)  # Wait for 5 seconds before next check
    except KeyboardInterrupt:
        sense.clear()
        print("Program terminated.")

if __name__ == "__main__":
    main()