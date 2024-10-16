from sense_hat import SenseHat
sense = SenseHat()

temp = sense.get_temperature()
print(f"Temperature: {temp:.2f} °C")