#
# Solution to Lesson 3, Exercise 1 on Accelerometer Gestures
#
# Filename: "accelTest1.py"
#

from microbit import *

display.show(Image.HAPPY)

while True:

    if accelerometer.is_gesture("shake"):
        display.show(Image.ANGRY)

    elif accelerometer.is_gesture("right"):
        display.show("R")

    elif accelerometer.is_gesture("left"):
        display.show("L")

    elif accelerometer.is_gesture("up"):
        display.show("U")

    elif accelerometer.is_gesture("down"):
        display.show("D")

    else:
        display.show(Image.HAPPY)

# EOF
