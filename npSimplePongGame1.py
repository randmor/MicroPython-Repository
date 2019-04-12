#
# "Microbit / MicroPixel Simple Pong Game, Ver 1"
#         Written by William Moore
#         of Walnut Creek, CA (USA)
#               April 9, 2019
#                   Enjoy!
#
# This program requires both the BBC Micro:bit board and the
# Proto-PIC (UK) "Micro:Pixel" display board. The Micro:Pixel
# board provides an 4x8 matrix display of what are essentially
# "smart" RGB LEDs that are chained together and controlled by
# a single GPIO pin (plus 3V and GND). These devices are called
# variously "NeoPixels", "ZIP LEDs", or "WS2812B LEDs".
#
# This game is written such that the Micro:bit/Micro:Pixel board
# combo has to be held in "portrait" orientation (turned 90 degrees
# clockwise from the "normal" (landscape) orientation). This first
# version of pong will ignore bouncing the "ball" off the sides of
# the display so we can better focus on the basics of the program.
#
# This game uses the Micro-bit's built-in accelerometer to sense
# right and left "tilt" gestures which will allow you to move
# the pong paddle. The "paddle" will be a blue pixel that moves
# horizontally along the bottom of the display (y = 7). The "ball"
# will be a yellow pixel that drops down along one of the 4 columns.
# If you hit the ball with the paddle, the ball will momentarily
# turn green before reversing its direction, and you will get a
# point. If you miss the ball, the ball will momentarily turn red
# and you will lose a point. The game ends when either you or the
# Microbit scores 6 points. If you win you'll see a green screen
# (and a happy face), and if you loose you'll see a red screen
# (and a sad face). The game will automatically restart after a 
# few seconds.
#
# filename = "npSimplePongGame1.py"

from microbit import *
from random import randint
import neopixel

np = neopixel.NeoPixel(pin0, 32) 

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
delay = 250

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

# display.scroll("MicroPixel Pong, ver 2")

# Display initial ball, blink ball 6 times
for i in range(0, 5):
    npPlot2(ballX, ballY, ballColor)
    np.show()
    sleep(speed)
    npPlot2(ballX, ballY, black)
    np.show()
    sleep(speed)

sleep(delay * randint(2, 7))
ballX = randint(0, 3)
npPlot2(ballX, ballY, ballColor)
np.show()
sleep(delay)
ballDirection = 1  # Falling

numScores = 6    # Change this if you want more rounds / game.
hitCount = 0
gameOn = True

while gameOn:
    
    sleep(delay)   # SLow down game to make easier to play
    
    # =======================
    #  Paddle Movement Code:
    # =======================
    
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

    npPlot2(oldPadX, 7, black)  # Turn-off LED at old paddle location
    npPlot2(padX, 7, padColor)  # Turn-on LED at new paddle location

    # =======================
    #   Ball Movement Code:
    # =======================
    
    # Save previous ball "x,y" location
    oldBallX = ballX
    oldBallY = ballY

    ballY = ballY + ballDirection           # Move ball down 1 more row

    # Case where paddle hit ball
    if ballY == 7 and padX == ballX:
        npPlot2(oldBallX, oldBallY, black)  # Turn off LED at old ball location
        npPlot2(ballX, ballY, colors[1])    # On hit, paint ball green
        np.show()
        sleep(250)
        ballDirection *= -1
        hitCount += 1                       # Increment score

        if hitCount >= numScores:            # When you have 21 hits you win!
            gameOn = False
            continue

    # Case where paddle missed ball
    elif ballY == 7 and padX != ballX:
        npPlot2(oldBallX, oldBallY, black)  # Turn off LED at old ball location
        npPlot2(ballX, ballY, colors[0])    # On miss, paint ball red
        np.show()
        sleep(delay)
        ballDirection *= -1
        hitCount -= 1                       # Decrement score
        
        if hitCount <= -numScores:           # When you have 21 hits you win!
            gameOn = False
            continue
        
        # Serve a new ball...
        ballY = 0
        ballX = randint(0, 4)           # Select new random column to serve ball in.
        sleep(randint(1, 5) * 100)      # Randomize delay before next ball serve. 
        
        npPlot2(oldBallX, oldBallY, black)  # Turn-off LED at old ball location
        npPlot2(ballX, ballY, colors[0])    # On miss, paint ball red
        np.show() 

    # Case where ball bounces back to top wall.
    elif ballY == 0:
        npPlot2(oldBallX, oldBallY, black)  # Turn-off LED at old ball location
        npPlot2(ballX, ballY, ballColor)    # Turn-on LED at old ball location
        np.show()
        sleep(speed)

        npPlot2(ballX, ballY, black)
        ballX = randint(0, 3)    # Select new random column to drop ball from.
        ballDirection *= -1
        npPlot2(ballX, ballY, ballColor)
        np.show()

    # Other cases where ball is either rising or falling
    else:
        npPlot2(oldBallX, oldBallY, black)  # Turn-off LED at old ball location
        npPlot2(ballX, ballY, ballColor)    # Turn-on LED at new ball location
        np.show()

    if button_a.is_pressed():
        display.scroll(hitCount)            # Show current score

# ==========[ End of "while gameOn:" loop ]==========

if hitCount >= numScores:       # You won!
    display.show(Image.HAPPY)   # Show "happy face" on 5x5 red LED display
    color = (0, mb, 0)          # Make color = green to signal a win.
else:                           # You lost!
    display.show(Image.SAD)     # Show "sad face" on 5x5 red LED display
    color = (mb, 0, 0)          # Make color = red to signal a loss.
    
for pix in range(len(np) - 1, 0, -3):  # Paint display either green or red 
    np[pix] = color                    # to signal a game win or loss.
    np.show()
    
sleep(2000)
reset()

# EOF
