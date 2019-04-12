'''
#
# Lesson #2: MicroPython & EduBlocks Programming Basics
#
# This file contains the source code to several MicroPython demo programs to be
# used in this second lesson. It also contains much of the lesson plan.
#
# To get the students to focus on the subject matter, begin Lesson #2 by viewing
# Shawn Hymel's second YouTube video called "Images, Buttons, and Conditionals"
# at this URL:
#
#       https://www.youtube.com/watch?v=XMr6Fg74fZY
#
# After the video, introduce the "Mu" editor for Microbit / MicroPython. Use the
# "big screen" monitor wth my laptop to show the kids the basics of using Mu to
# create, save, load and flash Python programs onto the Micro:bit. The demo program
# should also reinforce the video by focusing on the use of predefined images,
# button_a and button_b and the use of the if/elif/else conditional logic construct.
#

'''

#
# Lesson #2, Demo Progrm #1:
#
# This program will initially display a red "heart" image to show that the program
# has loaded and is running okay. It will then display a "Meh face". But, if you click
# on either button "A" or button"B", then it will display either a "Happy Face" or a
# "Sad Face" depending upon which push-button was pressed. You may need to "press & hold"
# the buttons to see the face changes. A really quick click may not be sensed by the
# program because of it's use of the sleep() function. We are using a relatively short
# delay of 1/3 a second, so this need to "press & hold" won't likely be needed, but if
# you make it a 2 or 3 second delay, then you will need to "press & hold".
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
    # order to get a happy or sad face?

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
    if button_a.is_pressed() and button_b.is_pressed() :
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

# With Demo Program #3 we explore how to create user-defined variables.
# There are two ways to lay out the user defined image definition in a
# text oriented Python program. Both methods are shown in demo program #3.
# The user defined image called "boat1" uses the multi-line approach
# which allows the programmer to more easily visualize which LEDs in the
# 5x5 red LED display are lit, and how bright they are. The second approach
# is a very succinct one liner as was used to define the "boat2" image.
# But, the easiest way is to ue the EduBlock's "Display / image" block
# command which you can easily translate to Python code and then cut and
# paster into your Python editor of choice.

'''

# Lesson #2, Demo Progrm #3:

# Program demonstrates how to create your own "used-defined" images.
#
# There are two ways to define a user-defined image: "single line" or
# "multi-line" with the latter allowing the programmer an easier way
# to visualize the pixels in his/her mind.
#
# Filename: Demo_L2-03.py

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
# For the remainder of the period, let the kids play with writing simple
# programs to create and view use-defined and pre-defined images, switching
# between images using button presses, etc. as shown above above.

# End of Lesson #2.
'''

# Note to self.  Add a demo program that counts the number of key presses,
# and chooses which image to display based on the number of Button A presses
# made in say 5 seconds. Then show the corresponding image. This exta demo
# is for maore advanced students.
