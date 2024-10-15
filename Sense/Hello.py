from sense_hat import SenseHat
sense = SenseHat()

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (160, 32, 240)

sense.show_message("S", scroll_speed=0.05, text_colour=red)
sense.show_message("a", scroll_speed=0.05, text_colour=orange)
sense.show_message("l", scroll_speed=0.05, text_colour=yellow)
sense.show_message("u", scroll_speed=0.05, text_colour=green)
sense.show_message("t", scroll_speed=0.05, text_colour=blue)
sense.show_message("a", scroll_speed=0.05, text_colour=purple)
sense.show_message("t", scroll_speed=0.05, text_colour=red)
sense.show_message("i", scroll_speed=0.05, text_colour=orange)
sense.show_message("o", scroll_speed=0.05, text_colour=yellow)
sense.show_message("n", scroll_speed=0.05, text_colour=green)
sense.show_message("s", scroll_speed=0.05, text_colour=blue)
