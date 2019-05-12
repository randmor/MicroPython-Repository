#
# Test/Demo program for TTP229 based 16-Key KeyPad
#
# Seems not to need the P1-3 jumper as indicated in the
# Hobby Components HCMODU0079_Arduino_Diagram.png image file
# (see second URL below). Originally, I had a problem where
# only the first 8 keys of the keypad were responsive, but
# erroneously gave me key numbers in the range of 9 to 16.
# I was able to fix the code to correct the number mismatch
# by counting only to 8 (or 9 as required by range() function).
# But, my goal was to get all 16 keys working, so I then
# soldered on the jumper headers to see if I could configure
# the keypad board to be responsive to all 16 keys. In doing
# that (but without using any actual jumpers) the keypad
# mysteriously started to work right -- all 16 keys were
# responsive. Fiddling with the hardware some more, the old
# problem came back. Since the software wasn't changed, I
# posted it up here for safe keeping on GitHub, and if anyone
# else wants to give it a try, go ahead... In the meantime,
# I think I will order a couple more of these boards to see if
# I can get them to work reliably on the Microbit to overcome
# some of the input limitations of the device.
#
# Here's the URL for the C/C++ demo I got from Hobby Components:
'''
http://forum.hobbycomponents.com/viewtopic.php?f=73&t=1781&hilit=hcmodu0079
http://hobbycomponents.com/images/forum/HCMODU0079_Arduino_Diagram.png

'''
#
# Filename: "TTP229_KeyPad_Demo.py"
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