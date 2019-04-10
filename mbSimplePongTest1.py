#
# My Simple Pong Game, version 1
# Written for the BBC Microbit and its 5x5 red LED dispaly
# April 9, 2019
#
# Filename = "mbSimplePong.py"

from microbit import display, Image, accelerometer, sleep, button_a, reset
from random import randint

maxScore = 6    # Change this if you want more rounds / game.
gestureSensitivity = 120
delay = 400

# Set initial position of pong game's "paddle"
padY = 4
padX = 2

# Display initial paddle
display.set_pixel(padX, padY, 9)

# Set initial position of pong game's "ball"
ballX = 0
ballY = 0

# Display initial ball, blink ball 3 times
# to attract the player's attention
for i in range(0, 3):
    display.set_pixel(ballX, ballY, 5)
    sleep(delay)
    display.set_pixel(ballX, ballY, 0)
    sleep(delay)

ballX = randint(0, 4)    # Randomly select column to serve ball in.
display.set_pixel(ballX, ballY, 5)

ballDirection = 1  # Falling  (-1 = Rising)
hitCount = 0
gameOn = True

while gameOn:

    sleep(delay)       # Makes game easier when slowed down a bit.

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

    # Make sure new x-coordinate is still in range (0 to 4)
    if padX < 0:
        padX = 0
    if padX > 4:
        padX = 4

    # Relative to the previous position of the lit pixel,
    # calculate y-axis change (if any) of the lit pixel.
    if yVal > gestureSensitivity:
        padY = oldPadY + 1
    elif yVal < -gestureSensitivity:
        padY = oldPadY - 1
    else:
        padY = oldPadY

    # Make sure new y-coordinate is still in range (0 to 4)
    if padY < 0:
        padY = 0
    if padY > 4:
        padY = 4

    # Test Code: Move paddle pixel anywhere on display
    # display.set_pixel(oldPadX, oldPadY, 0)    # Turn-off LED at old paddle position
    # display.set_pixel(padX, padY, 9)          # Turn-on LED at new paddle position

    # Limit paddle pixel to bottom row of the display
    display.set_pixel(oldPadX, 4, 0)          # Turn-off LED at old paddle position
    display.set_pixel(padX, 4, 9)             # Turn-on LED at new paddle position

    # =====================
    #  Ball Movement Code:
    # =====================

    # Save previous ball "x,y" location
    oldBallX = ballX
    oldBallY = ballY

    # Increment the ball's Y-axis value to make it drop one row down the display
    ballY = ballY + ballDirection

    # Case where paddle hit ball
    if ballY >= 4 and padX == ballX:

        hitCount += 1           # increment score
        ballDirection *= -1     # change ball direction

        # Check if player won...
        if hitCount >= maxScore:

            # Bounce the ball back to the top one last time
            for i in range(3, -1, -1):
                display.set_pixel(ballX, i, 5)
                sleep(delay)
                display.set_pixel(ballX, i, 0)

            #display.clear()
            sleep(delay)
            display.scroll("You won!")
            display.show(Image.HAPPY)
            sleep(3000)
            gameOn = False
            continue

    # Case where paddle missed ball
    elif ballY >= 4 and padX != ballX:
        display.set_pixel(oldBallX, oldBallY, 0)
        display.set_pixel(ballX, ballY, 5)      # turn-on LED at new ball location
        sleep(delay)
        display.set_pixel(ballX, ballY, 0))     # turn-off LED at new ball location

        hitCount -= 1             # Decrement score
        # ballDirection *= -1     # Change ball direction (up) [this line cancels out line 158]

        # Check if computer won...
        if hitCount <= -(maxScore):
            #display.clear()
            display.scroll("Game Over, computer won.")
            display.show(Image.SAD)
            sleep(3000)
            reset()

        # Serve a new ball...
        ballY = 0
        ballX = randint(0, 4)           # Select new random column to serve ball in.
        sleep(randint(1, 5) * 100)      # Randomize delay before next ball serve.
        
        display.set_pixel(oldBallX, oldBallY, 0)    # turn-off LED at old ball location
        display.set_pixel(ballX, ballY, 5)          # turn-on LED at new ball location
        # ballDirection *= -1    # change ball direction (down) [this line cancels out line 138]

    # Case where ball bounces back up to the top wall.
    elif ballY == 0:
        display.set_pixel(oldBallX, oldBallY, 0)    # turn-off LED at old ball location
        display.set_pixel(ballX, ballY, 5)          # turn-on LED at new ball location
        sleep(delay)
        display.set_pixel(ballX, ballY, 0)          # turn-off LED at new ball location
        
        ballX = randint(0, 4)      # Select new random column to serve ball in.
        ballDirection *= -1
        sleep(randint(1, 5) * 100) # Randomize delay before next ball serve.

        display.set_pixel(ballX, ballY, 5)

    # Other cases where ball is either rising or falling
    else:
        # Debug code:
        print("ballY = " + str(ballY))       # View print() output using REPL

        display.set_pixel(oldBallX, oldBallY, 0)    # turn-OFF LED at old ball location
        display.set_pixel(ballX, ballY, 5)      # turn-on LED at new ball location

    # Make ball speed-up as it falls and slow-down as it rises.
    # delay = 128 - 16 * ballX   # was 8
    # sleep(delay)

    if button_a.is_pressed():
        display.scroll(hitCount)            # Show current score

# End of "while gameOn:" loop
# ===========================
# Restart game after 3 seconds
sleep(3000)
reset()
#
# EOF
