from sense_hat import SenseHat
import time

sense = SenseHat()

#while True:
#	temp = sense.get_temperature()
#     sense.show_message(f"{temp:.1f}C", scroll_speed=0.05)
#	 time.sleep(2)

temp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

print(f"Temperature:{temp:.2f}C")
print(f"Humidity:{temp:.2f}%")
print(f"Pressure:{pressure:.2f} hPa")
