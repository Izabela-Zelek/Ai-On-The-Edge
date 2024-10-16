from sense_hat import SenseHat
sense = SenseHat()

pressure = sense.get_pressure()
print(f"Pressure: {pressure:.2f} hPa")