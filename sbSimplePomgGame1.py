#
#     "Scroll:Bit Simple Pong Game, Version 1"
#        Written for the BBC Microbit coupled 
#        with the Pimoroni Scroll:Bit display
#            Written by: William Moore
#            of Walnut Creek, CA (USA)
#                April 10, 2019
#                    Enjoy!
#`
# I was running up against memory errors, so I trimmed out a few features.
#
# One bug that remains occurs when the paddle misses the ball. I can correct
# for it, but problem should not be occuring. The debug (fix) code is still 
# enabled. See code around lines 206 to 215. I will try to figure out the bug 
# and correct it. If you spot the problem in my code, let me know so I can 
# fix it properly.
#
# Filename = "sbSimplePongGame1.py"

from microbit import display, Image, accelerometer, sleep, button_a, reset
from futz import set_pixel, show, clear
from random import randint

def plot(x, y, intensity):
    set_pixel(x, y, intensity)
    show()

# Define happy & sad faces turned sideways
hapFace = Image("00090:09009:00009:09009:00090")
sadFace = Image("00009:09090:00090:09090:00009")

# Define 7 brightness levels
brightness = [0, 5, 10, 20, 40, 80, 160]

maxScore = 6    # Change this if you want more rounds / game.
gestureSensitivity = 120
delay = 128

# Set initial position of pong game's "paddle"
padX = 16
padY = 3

# Display initial paddle
plot(padX, padY, brightness[4])

# Set initial position of pong game's "ball"
ballX = 0
ballY = 6

# Display initial ball, blink ball 3 times
# to attract the player's attention
for i in range(0, 3):
    plot(ballX, ballY, brightness[2])
    sleep(delay)
    plot(ballX, ballY, brightness[0])
    sleep(delay)

ballY = randint(0, 6)
plot(ballX, ballY, brightness[2])
ballDirection = 1  # Falling  (-1 = Rising)
hitCount = 0
gameOn = True

while gameOn:
    clear()
    display.clear()

    # Modify game timing to adjust game "hardness/easiness"
    sleep(delay)       # Makes game easy
    # sleep(delay//2)    # Not so easy
    # sleep(delay//4)    # Moderate
    # sleep(delay//8)    # Harder
    # no 'sleep(delay)' == Hardest

    # Get accelerometer's x-axis and y-axis values so we can move
    # the paddle around using accelerometor's x,y coordinates
    xVal = accelerometer.get_x()
    yVal = accelerometer.get_y()

    # =======================
    #  Paddle Movement Code:
    # =======================

    # Save previous paddle "x,y" location.
    oldPadX = padX
    oldPadY = padY

    # Relative to the previous position of the lit pixel,
    # calculate x-axis change (if any) of the lit pixel.
    if xVal > gestureSensitivity:
        padX = oldPadX + 1
    elif xVal < -gestureSensitivity:
        padX = oldPadX - 1
    else:
        padX = oldPadX

    # Make sure new x-coordinate is still in range (0 to 16)
    if padX < 0:
        padX = 0
    if padX > 16:
        padX = 16

    # Relative to the previous position of the lit pixel,
    # calculate y-axis change (if any) of the lit pixel.
    if yVal > gestureSensitivity:
        padY = oldPadY + 1
    elif yVal < -gestureSensitivity:
        padY = oldPadY - 1
    else:
        padY = oldPadY

    # Make sure new y-coordinate is still in range (0 to 6)
    if padY < 0:
        padY = 0
    if padY > 6:
        padY = 6

    # Test Code: Move pixel anywhere on display
    # plot(padX, padY, brightness[4])

    # Move paddle pixel Left/Right on row 16 (in portrait mode)
    plot(16, padY, brightness[4])

    # =====================
    #  Ball Movement Code:
    # =====================

    # Save previous ball "x,y" location
    oldBallX = ballX
    oldBallY = ballY

    ballX = ballX + ballDirection

    # Case where paddle hit ball
    if ballX >= 16 and padY == ballY:

        display.show(hapFace)
        sleep(250)

        hitCount += 1           # increment score
        ballDirection *= -1     # change ball direction

        # Check if player won...
        if hitCount >= maxScore:

            # Bounce the ball back to the top one last time
            for i in range(15, -1, -1):
                plot(i, ballY, brightness[2])
                sleep(128 - 8 * i)
                plot(i, ballY, brightness[0])

            clear()
            sleep(delay)
            display.scroll("You won!")
            display.show(hapFace)
            sleep(3000)
            gameOn = False
            continue

    # Case where paddle missed ball
    elif ballX >= 16 and padY != ballY:

        # plot last ball
        plot(ballX, ballY, brightness[2])

        display.show(sadFace)
        sleep(250)

        hitCount -= 1                       # Decrement score
        # ballDirection *= -1                 # change ball direction (up)

        # Check if computer won...
        if hitCount < -(maxScore):
            clear()
            display.scroll("Game Over, computer won.")
            display.show(sadFace)
            sleep(3000)
            reset()

        # Serve a new ball...
        ballX = 0
        ballY = randint(0, 6)               # Select new random column to serve ball in.
        sleep(randint(1, 5) * 100)          # randomize delay before next ball serve.
        plot(ballX, ballY, brightness[2])
        # ballDirection *= -1                 # change ball direction (down)

    # Case where ball bounces back up to the top wall.
    elif ballX == 0:
        plot(ballX, ballY, brightness[2])   # display last ball at top of column
        sleep(delay)
        plot(ballX, ballY, brightness[0])   # turn off last ball

        ballY = randint(0, 6)               # Select new random column to serve ball in.
        ballDirection *= -1
        sleep(randint(1, 5) * 100)          # randomize delay before next ball serve.
        plot(ballX, ballY, brightness[2])

    # Other cases where ball is either rising or falling
    else:
        # Debug code:
        print("ballX =" + str(ballX))       # View print() output using REPL

        plot(ballX, ballY, brightness[2])

    # Make ball speed-up as it falls and slow-down as it rises.
    delay = 128 - 8 * ballX
    sleep(delay)

    if button_a.is_pressed():
        display.scroll(hitCount)            # Show current score

    # Debug code:  Seems something is making ballX > 16. Should not be.
    if ballX > 16:

        for i in range(0,6):
            display.set_pixel(0,0,0)        # Signal error
            sleep(500)
            display.set_pixel(0,0,9)
            sleep(500)

        ballX = 16      # my "fix" (now sad face "blinks")

# End of "while gameOn:" loop
# ===========================
# Press Micro:bit's "Reset" button for a new game.

# EOF


