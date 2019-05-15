#
# Sample MicroPython Program to Test Circuit
#
# Uses a single analog input and a voltage divider "network"
# of resistors layed out in such a way that each key closure
# will present a different voltage value to the analog input
# and the "driver" program can figure out which key is which
# depending on the voltage read in on the analog input pin.
#
# In this example we will be using Microbit "pin0" as the
# analog input pin to which the keypad output is attached.
#
# Filename = "keypadTest1.py"
#

from microbit import *

thresholds = [4, 72, 131, 185, 255, 295, 329, 362, 408, 433, 456, 478, 510, 528, 544, 560]
keyNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def getKey():
    keyValue = pin0.read_analog()
    for i in range(0,16):
        # Is key value close to any one of the threshold values?
        if abs(keyValue - thresholds[i]) < 5:
            return keyNum[i]

            # Wait untl user releases keypad button
            # while pin0.read_analog() < 1000:
                # sleep(100);

display.show(Image.HAPPY)
sleep(1000)

while True:
    key = getKey()
    if key is not None:
        display.scroll(str(key))
    sleep(500)