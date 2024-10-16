from sense_hat import SenseHat
import time
import math

sense = SenseHat()

def calculate_heat_index(temperature, humidity):
    T = temperature
    R = humidity
    HI = 0.5 * (T + 61.0 + ((T - 68.0) * 1.2) + (R * 0.094))
    if HI >= 80:
        HI = -42.379 + 2.04901523*T + 10.14333127*R - 0.22475541*T*R - 0.00683783*T*T - 0.05481717*R*R + 0.00122874*T*T*R + 0.00085282*T*R*R - 0.00000199*T*T*R*R
    return HI

temp = sense.get_temperature()
humidity = sense.get_humidity()
heat_index = calculate_heat_index(temp, humidity)

green = (0, 255, 0) # Comfortable
red = (255, 0, 0) # Uncomfortable

if 18 <= heat_index <= 24:
    sense.show_message("Comfy :)", scroll_speed=0.05, text_colour=green)
else:
    sense.show_message("No comfy >:(", scroll_speed=0.05, text_colour=red)