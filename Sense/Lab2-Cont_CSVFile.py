from sense_hat import SenseHat
import csv
import time
sense = SenseHat()
with open('sensor_data_continuous.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)", "Pressure (hPa)"])
    try:
        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            temp = sense.get_temperature()
            humidity = sense.get_humidity()
            pressure = sense.get_pressure()
            writer.writerow([timestamp, f"{temp:.2f}", f"{humidity:.2f}", f"{pressure:.2f}"])
            print(f"Data logged at {timestamp}")
            time.sleep(5)
    except KeyboardInterrupt:
     print("Data logging stopped by user.")