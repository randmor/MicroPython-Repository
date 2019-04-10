#
#   "Microbit / MicroPixel Simple Pong Game, Version 2"
#       Written by William Moore
#           of Walnut Creek, CA (USA)
#               April 10, 2019
#                   Enjoy!
#
# This program requires both the BBC Micro:bit board coupled with 
# the Proto-PIC "Micro:Pixel" display board. The Micro:Pixel board 
# provides an 4x8 matrix display of what are essentially "smart" 
# RGB LEDs that are chained together and controlled by a single 
# GPIO pin (plus 3V and GND). These devices are called variously 
# "NeoPixels", "ZIP LEDs", or "WS2812B LEDs".
#
# This game is written such that the Micro:bit / Micro:Pixel board
# combo has to be held in "portrait" orientation (turned 90 degrees
# clockwise from the "normal" (landscape) orientation). This simple 
# version of pong ignores bouncing the "ball" off the sides of the 
# so we can better focus on the basics of the program.
#
# Also in version 2, I have integrated music and sound effects into
# this pong game program. Be aware that I have modified my Proto-PIC 
# MicroPixel board to use "pin8" instead of "pin0" since I'm now 
# using "pin0" to drive a speaker. This modification involves a 
# trace cut and a blob-of-solder "jumper", and is documented on 
# the Proto-PIC webpage that describes this product. My code is 
# now running pretty well. I did encounter a bug where the sound 
# generated by the music.pitch() method would cut-off (no sound 
# for a while) when using higher pitches (maybe above 1000?!). I 
# was able to program around this bug by using lower pitched 
# notes (below 1000).
#
# Filename: "npSimplePongGame2.py"

from microbit import *
from random import randint
import neopixel
import music

np = neopixel.NeoPixel(pin8, 32)

# Enable x,y coordinates to work with Microbit in landscape orientation.
def npPlot1(x, y, color):
    np[31-x-abs(y+4)*8] = color

# Enable x,y coordinates to work with Microbit in portait orientation.
def npPlot2(x, y, color):
    np[31-y-abs(x-3)*8] = color

mb = 32     # define maximum LED brightness

# Define a Python list of useful RGB colors. These colors
# include RED, GRN, BLU, ORG, YEL, CYN, MAG, and WHT.
colors = [(mb, 0, 0),  (0, mb, 0),  (0, 0, mb),  (mb, mb/2, 0),
          (mb, mb, 0), (0, mb, mb), (mb, 0, mb), (mb, mb, mb)]

black = (0, 0, 0)

gestureSensitivity = 128
speed = 100

music.play(music.RINGTONE)

# Set initial position of pong game's "paddle"
padX = 2

# Set color of pong game's "paddle" to blue
padColor = colors[2]

# Display initial paddle
npPlot2(padX, 7, padColor)
np.show()

# Set initial position of pong game's "ball"
ballX = 0
ballY = 0

# Set color of pong game's "ball" to yellow
ballColor = colors[4]

# display.scroll("MicroPixel Pong Ver2")

# Display initial ball, blink ball 6 times
for i in range(0, 5):
    npPlot2(ballX, ballY, ballColor)
    np.show()
    sleep(speed)
    npPlot2(ballX, ballY, black)
    np.show()
    sleep(speed)

sleep(speed * randint(2, 7))
ballX = randint(0, 3)
npPlot2(ballX, ballY, ballColor)
np.show()
sleep(speed)
ballDirection = 1  # Falling
numScores = 6
hitCount = 0
gameOn = True

while gameOn:

    '''
    Paddle Movement Code:
    '''
    # Get accelerometer's x-axis and y-axis values.
    # I had to switch yVal and xVal around to get
    # the program to behave properly in portait mode.

    # Don't change 'y' coordinate as paddle lives on row 7.
    # yVal = accelerometer.get_x()
    xVal = accelerometer.get_y()    # But paddle does move left & right.

    # Save previous paddle "x,7" location.
    # Paddle will always be on bottom row of the display, so no
    # need for am "oldPadY" variable.
    oldPadX = padX

    # Relative to the previous position of the lit pixel,
    # calculate x-axis change (if any) of the lit pixel.
    if xVal > gestureSensitivity:
        padX = oldPadX - 1
    elif xVal < -gestureSensitivity:
        padX = oldPadX + 1
    else:
        padX = oldPadX

    # Make sure new x-coordinate is still in range (0 to 3)
    if padX < 0:
        padX = 0
    if padX > 3:       # The x-coordinate range is now "0..3"
        padX = 3

    npPlot2(oldPadX, 7, black)
    npPlot2(padX, 7, padColor)

    '''
    Ball Movement Code:
    '''
    # Save previous ball "x,y" location
    oldBallX = ballX
    oldBallY = ballY

    ballY = ballY + ballDirection

    # Case where paddle hit ball
    if ballY == 7 and padX == ballX:
        npPlot2(oldBallX, oldBallY, black)  # Turn-off LED at old ball location
        npPlot2(ballX, ballY, colors[1])    # On hit, paint ball green
        np.show()

        # Use two short beeps at high pitch to indicate a "hit"
        music.pitch(880, 100)
        sleep(50)
        music.pitch(990, 100)

        ballDirection *= -1
        hitCount += 1              # Increment score

        if hitCount >= numScores:  # When you have "numScores" hits you win!
            gameOn = False
            continue

    # Case where paddle missed ball
    elif ballY == 7 and padX != ballX:
        npPlot2(oldBallX, oldBallY, black)  # Turn-off LED at old ball location
        npPlot2(ballX, ballY, colors[0])    # On miss, paint ball red
        np.show()

        # Use one long beep at low pitch to indicate a "miss".
        music.pitch(110, 250)

        ballDirection *= -1
        hitCount -= 1               # Decrement score

        if hitCount <= -numScores:  # If true, computer wins!
             gameOn = False
             continue

# Case where ball bounces back to top wall.
    elif ballY == 0:
        music.pitch(440 + ballY * 32, 100)
        npPlot2(oldBallX, oldBallY, black)  # Turn-off LED at old ball location
        npPlot2(ballX, ballY, ballColor)    # Turn-on LED at new ball location 
        np.show()
        sleep(speed)
        np.show()
        npPlot2(ballX, ballY, black)
        ballX = randint(0, 3)    # Select new random column to drop ball from.
        ballDirection *= -1
        npPlot2(ballX, ballY, ballColor)
        np.show()
    # Other cases where ball is either rising or falling
    else:
        # Add music note that varies according to ballY.
        music.pitch(440 + ballY * 32, 100)
        npPlot2(oldBallX, oldBallY, black)  # Turn-off LED at old ball location
        npPlot2(ballX, ballY, ballColor)    # Turn-on LED at new ball location
        np.show()
        sleep(speed)
    if button_a.is_pressed():
        display.scroll(hitCount)            # Show current score

# ==========[ End of "while gameOn:" loop ]==========
if hitCount >= numScores:       # You won!
    display.show(Image.HAPPY)   # Show "happy face" on 5x5 red LED display
    color = (0, mb, 0)          # Make color = green to signal a win.

else:                           # You lost!
    display.show(Image.SAD)     # Show "sad face" on 5x5 red LED display
    color = (mb, 0, 0)          # Make color = red to signal a loss.

for pix in range(0, len(np)):   # Paint display either green or red to
    np[pix] = color             # signal a game win or loss.
    np.show()

# Play a tune as a reward (or as punishment).
if hitCount >= numScores:
    music.play(music.PYTHON)
else:
    music.play(music.FUNERAL)

np.clear()
reset()

# EOF