#
# Test/Demo program for TTP229 based 16-Key KeyPad
#
# Works okay for keys 1-8 if MAX = 8. When MAX = 16,
# the keys marked 1 thru 8 return values 9 thru 16 and
# keys marked 9 thru 16 return nothing. Is likely a
# keypad configuration problem, need to research more.
#
# If I jumper P1-3, keypad forever returns "11". So, the
# Arduino-to-Keypad wiring diagram image showing how the
# keypad board should be jumpered seems wrong. Here's that URL:
'''
http://forum.hobbycomponents.com/viewtopic.php?f=73&t=1781&hilit=hcmodu0079
http://hobbycomponents.com/images/forum/HCMODU0079_Arduino_Diagram.png

'''
# This is my second attempt to rewrite C/C++ script
# into MicroPython so I can use this 16-key keypad on
# the BBC Microbit/MicroPython platform.
#
# Filename: keyPadTest2.py"
#

from microbit import *

# MAX = 9     # Use for keys 1-8 (i.e. an 8-key keypad)
MAX = 17    # Use for keys 1-16 (i.e. a 16-key keypad)

def readKeypad():       # Function to read the keypad

    keyNum = 0

    # Toggle the clock pin 16 times (one for each key of the keypad)
    #  and read the state of the data pin on each pulse.
    for count in range(1, MAX):

        # Set clock signal low
        pin1.write_digital(0)

        # If the data pin is low (active low mode) then store the
        # current key number.
        if pin2.read_digital() != 1:
            keyNum = count

        # Set clock signal high
        pin1.write_digital(1)

    return keyNum

display.scroll("Testing Keypad:")

while True:
    key = readKeypad()

    if key != 0:
        display.scroll("=" + str(key))
        sleep(100)

# EOF