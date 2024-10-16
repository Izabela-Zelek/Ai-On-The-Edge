import matplotlib.pyplot as plt
import csv
import datetime

filename = input("Enter the CSV filename (including .csv extension): ") #20241015-230559_sensor_data.csv

timestamps = []
temperatures = []
humidities = []
pressures = []

with open(filename, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        timestamps.append(datetime.datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S"))
        temperatures.append(float(row["Temperature (°C)"]))
        humidities.append(float(row["Humidity (%)"]))
        pressures.append(float(row["Pressure (hPa)"]))
        
plt.figure(figsize=(12, 6))
plt.plot(timestamps, temperatures, label='Temperature (°C)', color='red', marker='o')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(timestamps, humidities, label='Humidity (%)', color='blue', marker='x')
plt.xlabel('Time')
plt.ylabel('Humidity (%)')
plt.title('Humidity Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(timestamps, pressures, label='Pressure (hPa)', color='green', marker='s')
plt.xlabel('Time')
plt.ylabel('Pressure (hPa)')
plt.title('Pressure Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()