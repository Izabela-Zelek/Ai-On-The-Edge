from sense_hat import SenseHat
import csv
import time
sense = SenseHat()
with open('sensor_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)", "Pressure (hPa)"])
 
    for i in range(10):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        temp = sense.get_temperature() 
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        writer.writerow([timestamp, f"{temp:.2f}", f"{humidity:.2f}", f"{pressure:.2f}"])
        print(f"Data logged at {timestamp}")
        time.sleep(5) # Wait for 5 seconds