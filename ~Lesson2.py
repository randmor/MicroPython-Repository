'''
#
# Lesson #2: MicroPython & EduBlocks Programming Basics
#
# This file contains the source code to several MicroPython demo programs to be
# used in this second lesson. It also contains much of the lesson plan.
#
# Part 1: Video & MicroPython: Images, Buttons, and Conditionals
#
# To get the students to focus on the subject matter, begin Lesson #2 by viewing
# Shawn Hymel's second YouTube video called "Images, Buttons, and Conditionals"
# at this URL:
#
#       https://www.youtube.com/watch?v=XMr6Fg74fZY
#
# Part 2: The Mu Editor
#
# After the video, introduce the "Mu" editor for Microbit / MicroPython. Use the
# "big screen" monitor wth my laptop to show the kids the basics of using Mu to
# create, save, load and flash Python programs onto the Micro:bit. The demo program
# should also reinforce the video by focusing on the use of predefined images,
# button_a and button_b and the use of the if/elif/else conditional logic construct.
#

'''

#
# Lesson #2, Demo Program #1:
#
# This program will initially display a red "heart" image to show that the program
# has loaded and is running okay. It will then display a "Meh face". But, if you click
# on either button "A" or button "B", then it will display either a "Happy Face" or a
# "Sad Face" depending upon which push-button was pressed. You may need to "press & hold"
# the buttons to see the face changes. A really quick click on a button may not be sensed 
# by the program because of it's use of the sleep() function. We are using a relatively 
# short delay of 1/3 a second, so this need to "press & hold" won't likely be needed, but
# if you make it a 2 or 3 second delay, then you will need to "press & hold".
#

from microbit import *

display.show(Image.HEART)     # Show that the program has loaded and is running.
sleep(2000)                   # Give the user a couple seconds to view the image.

while True:
    display.show(Image.MEH)

    if button_a.is_pressed():
        display.show(Image.HAPPY)

    if button_b.is_pressed():
        display.show(Image.SAD)

    # Comment-out the following "sleep(333)" statement by adding a hash mark (#)
    # just before the "s" in "sleep(333)", and see what happens when you run the
    # program.

    # After that test, un-comment the line and change it to read "sleep(3000)"
    # and see what happens when you run the program. What do you have to do in
    # order to get a happy or sad face?   (Answer: "press & hold" the button.)

    sleep(333)      	

# EOF

'''
# In this second demo program we show how we can detect the special event where
# both button "A" and button "B" are pressed at the same time. Notice how the
# logical "and" operator is used to combine the previous two button's is_pressed()
# statements into one long expression. With the "and" operator, both conditional
# statements must evalutate to True in order to execute the block of indented
# commands following the "if" statement.
#
# This second demo also shows how to use a variable called "delay" to set the
# sleep() function's sleep time so that we only have to change the code in one
# place to affect this sleep time change everywhere it is used in the program.
#
# Be sure to explain that a "variable" is a "named area in memory where data can
# be stored and referenced later in the programs just by using the variable's name".
# Python variables can hold different types of data, including integer (whole)
# numbers, floating point numbers, strings, and Booleans. Be sure to explain these
# 4 types of data so the students can recognize the type of data they are dealing
# with. Later they will have to recognize the data types they are working with when
# they have to convert data of one type to data of another type.

'''

# Lesson #2, Demo Program #2:

from microbit import *

delay = 2000

display.show(Image.HEART)     # Show program has loaded and is running.
sleep(delay)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.SURPRISED)
        sleep(delay//4)

    elif button_a.is_pressed():
        display.show(Image.HAPPY)
        sleep(delay//4)

    elif button_b.is_pressed():
        display.show(Image.SAD)
        sleep(delay//4)
    else:
        display.show(Image.MEH)
        sleep(delay//4)

# EOF

'''

# How might we improve the program above? See any repeated lines of code?
# How can we reduce those 4 "sleep(delay//4) commands down to one?
# Here's the answer:

'''

# Lesson #2, Demo Program #2B:

from microbit import *

delay = 2000

display.show(Image.HEART)     # Show program has loaded and is running.
sleep(delay)

while True:
    if button_a.is_pressed() and button_b.is_pressed() :
        display.show(Image.SURPRISED)

    elif button_a.is_pressed():
        display.show(Image.HAPPY)

    elif button_b.is_pressed():
        display.show(Image.SAD)

    else:
        display.show(Image.MEH)

    sleep(delay//4)

# EOF

'''

# With Demo Program #3 we explore how to create user-defined images.
# There are two ways to lay-out the user-defined image definition in a
# text oriented Python program. Both methods are shown in demo program #3.
# The user-defined image called "boat1" uses the multi-line approach
# which allows the programmer to more easily visualize which LEDs in the
# 5x5 red LED display are lit, and how bright they are. The second single 
# line approach is a very succinct way to define a user-defined image that
# is more difficult to read, but saves space in the source code listing. 
# Notice that the "boat2" image is defined using this single-line format.
#
# But, the easiest way to define a user-defined image is to use EduBlock's 
# "Display / image" block command that makes it easy to view which LED will 
# be lit (and to what brightness), and you can easily translate it to Python 
# code and then "cut and paste" the line of code into your Python editor.

'''

# Lesson #2, Demo Program #3:

# This program demonstrates how to create your own "used-defined" images.
#
# There are two ways to define a user-defined image: "single line" or
# "multi-line" with the latter allowing the programmer an easier way
# to visualize the pixels in his/her mind.
#

from microbit import *

# The multi-line list definition allows you to visualize
# your image in your "mind's eye" more easily:

boat1 = Image("05050:"
              "05050:"
              "05050:"
              "99999:"
              "09990")

# The single line list definition is more succinct.
# Note boat2's pixel data is for lower light intesity than boat1.

boat2 = Image("01010:01010:01010:55555:05550")

while True:
    display.show(boat1)
    sleep(3000)

    display.clear()
    sleep(500)

    display.show(boat2)
    sleep(3000)

    display.clear()
    sleep(500)

# EOF

'''
# How to select between more than three items on the Microbit?
#
# Well, you could add more buttons using the GPIO Pins, but sometimes that 
# is too much trouble. Another method is to have the user press a button "n" 
# times, and use the value of "n" to select between your options. This is 
# possible by using the "button_a.get_presses()" or button_b.get_presses()
# methods as shown in Demo #4, below.
#
# The source code for Demo #4 lists most of the predefined images as they are
# being appended to the "myFavImages" array. Each image being appended also has 
# an in-line comment specifying the index number for that image within the array.
# The program then gives the user a chance to click the "A" button a bunch of times 
# to select the desired image to be displayed. For instance, the "RABBIT" image 
# has the index of 12, so if you click the "A" button 12 times, the program wi;;
#display the selected image (i.e. the "RABBIT" image). This method of input allows 
# people a method for selecting between a relatively large number of options 
# without resorting to adding a bunch of buttons to the Microbit. It will help to 
# have a printed selection menu and a well designed user interface to help the 
# user through the selection process. Run Demo Program #4 to see how the UI works.
#
'''

# Lesson #2, Demo Program #4:
#
# This program is designed to allow the user to view specific 
# predefined images by clicking the "A" button the number of 
# times equivalent to that image's index within the 
# myFavImages list. 
#
# Images NOT displayed include the collection of 8 direction-arrow
# images and the collection of 12 clockhand images.
#
# Filename: "viewSelectedImage.py"

from microbit import *

# Define a Python list (aka "array") and fill it 
# with my favorite predefined images.

myFavImages = []                       # Index Numbers

myFavImages.append(Image.HEART)        #  0
myFavImages.append(Image.HAPPY)        #  1
myFavImages.append(Image.SAD)          #  2
myFavImages.append(Image.MEH)          #  3
myFavImages.append(Image.ASLEEP)       #  4
myFavImages.append(Image.SURPRISED)    #  5
myFavImages.append(Image.SILLY)        #  6
myFavImages.append(Image.CONFUSED)     #  7
myFavImages.append(Image.ANGRY)        #  8
myFavImages.append(Image.CHESSBOARD)   #  9
myFavImages.append(Image.SQUARE)       # 10
myFavImages.append(Image.DIAMOND)      # 11
myFavImages.append(Image.RABBIT)       # 12
myFavImages.append(Image.COW)          # 13
myFavImages.append(Image.DUCK)         # 14
myFavImages.append(Image.TORTOISE)     # 15
myFavImages.append(Image.BUTTERFLY)    # 16
myFavImages.append(Image.GIRAFFE)      # 17
myFavImages.append(Image.SNAKE)        # 18
myFavImages.append(Image.HOUSE)        # 19
myFavImages.append(Image.PITCHFORK)    # 20
myFavImages.append(Image.XMAS)         # 21
myFavImages.append(Image.PACMAN)       # 22
myFavImages.append(Image.TARGET)       # 23
myFavImages.append(Image.TSHIRT)       # 24
myFavImages.append(Image.ROLLERSKATE)  # 25
myFavImages.append(Image.SWORD)        # 26
myFavImages.append(Image.STICKFIGURE)  # 27
myFavImages.append(Image.GHOST)        # 28
myFavImages.append(Image.SKULL)        # 29
myFavImages.append(Image.UMBRELLA)     # 30
myFavImages.append(Image.SMILE)        # 31
myFavImages.append(Image.YES)          # 32
myFavImages.append(Image.NO)           # 33

'''
# Display all 34 predefined images listed above:
for image in myFavImages:
    display.show(image)
    sleep(1000)
'''

while True:
    
    # Clear 'btnPressCounter' within the button_a object
    pressCount = button_a.get_presses() 
    
    # Click Button "B" when ready to start...
    display.show(Image.ARROW_E)
    while True:
        if button_b.is_pressed():
            break
        sleep(1000)
    
    # Give user a count down... and 15 seconds to click Button "A" as many times as needed.
    # To view the GIRAFFE image, you will need to press Button "A" 17 times.
    display.show(3)
    sleep(500)
    display.show(2)
    sleep(500)
    display.show(1)
    sleep(500)
    display.show(Image.TARGET)
    
    # Click Button "B" again when you are finished clicking on Button "A" to
    # select the specific image to display.
    while True:
        if button_b.is_pressed():
            break
        sleep(1000)
    
    display.clear()
    
    pressCount = button_a.get_presses()
    
    if pressCount > 32:
        pressCount = 32 	# To avoid an indexing error
    
    display.scroll(pressCount)
    sleep(1000)
    
    display.show(myFavImages[pressCount])
    sleep(5000)

'''
# For the remainder of the period, let the kids play with writing simple
# programs to create and view use-defined and pre-defined images, switching
# between images using button presses, etc. as shown above above.

# End of Lesson #2.
'''
# EOF
