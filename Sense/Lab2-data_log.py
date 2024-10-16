from sense_hat import SenseHat
import csv
import time

sense = SenseHat()
filename = time.strftime("%Y%m%d-%H%M%S") + "_sensor_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)", "Pressure (hPa)"])
    
interval = 10
try:
    while True:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        temp = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, f"{temp:.2f}", f"{humidity:.2f}", f"{pressure:.2f}"])

        print(f"Data logged at {timestamp}")
        time.sleep(interval)
except KeyboardInterrupt:
 print("Data logging stopped by user.")