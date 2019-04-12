'''
#
# Lesson #1: Introduction to the BBC Microbit and MicroPython
#
# This file contains the source code to several MicroPython demo programs
# to be used in this first lesson. It also contains much of the lesson plan.
#
# Part 1: Video & Into to the BBC Micro:bit and MicroPython
#
# To get the students to focus on the subject matter, begin Lesson #1 by
# viewing Shawn Hymel's YouTube video called "Getting Started" at this URL:
#
#       https://www.youtube.com/watch?v=ZIW_6rxYNBg
#
# After the video, discuss the Micro:bit and MicroPython in more detail, 
# answering questions students may have. Since the video is rather "dense" 
# in new "techno-babble", it may be worth a second watch.
#
# Using the "big screen" computer, show the students how to create the
# "Hello, World!" program using the Microbit On-line Python Editor at this URL:
#
#       https://python.microbit.org/v/1.1
#
# Make sure each student understands how to:
#
#       1.) Enter a new program,
#       2.) Save their program,
#       3.) Load their program,
#       4.) Download and run their program on the Microbit
#
# Since this process is about as clear as "mud" to new students, give them
# time to do this exercise on their own and go around to each student to
# make sure they know how to do this exercise. Have them try it on other
# programs listed below.
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

   Review Safety with the Students...

    1.) Use the Microbit on top of some non-conductive surface like a wooden
	table, a 1-foot square piece of cardboard or sheet of plastic. This is
	important because it is very easy to accidently short-out the Microbit
	board if you lay it on a metal table or on some other metal object(s).
	For this same reason, don't place metal objects on or near the Microbit
	board. We don't want you to damage your board. If you damage your
	Microbit board, you (or your parents) will have to buy a replacement,
	which costs about $20.00.

    2.) Don't play with the Microbit board in the bathtub, shower, pool or out
	in the rain as water conducts electricity extremely well and electrical
	shock can damage your Microbit board and may pose a shock hazard to you.
	Water and electrical/electronic device do not mix well. Also, avoid
	spilling any liquids (such as your drink) on the Microbit board. Keep
	you drinking glass far away to avoid knocking it over with your elbow.

    3.) The +5V USB power (from your computer) and the regulated 3V power supply
	on the Microbit board do not really pose a risk of shock unless, perhaps,
	there is water involved. Even with water involved, the risk of electo-
	cution is very unlikely, though you may feel a slight shock under the
	right conditions. Compared to the very real risk of electrocution that
	can happen when playing with 120V AC (from wall sockets, overhead lights,
	etc,) the risk of electocution using AA and AAA batteries is virtually
	non-existant (but, "never say never").

    4.) Get in the habit of handling the Microbit by holding the edges of the board,
	since on dry days, there may be static electricity built up in your body
	and such static shock can damage the board. Remind the kids of when they
        rub their socks on a carpeted floor and then touch a door knob and get
        a shock on dry weather days. That's the kind of shock that will damage
        these boards. On such days, you should ground yourself before picking
	up any PCB including the Microbit board.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#
# Part 2: EduBlocks for Microbit / MicroPython:
#
# If time allows, show students how to use EduBlocks, and how to save their
# block code files as .xml files, and how to load them again. SHow the students
# how to convert the block code to Python text code and back again. Show how to
# download their programs as .hex code and run them on the Microbit using the same
# process as the Python Online Editor. EduBlocks for the Microbit can be found
# at the following URL:
#
#       https://microbit.edublocks.org/
#
# Be sure to show the students the 1-to-1 correspondance between EduBlock block
# commands and the MicroPython text commands. Tell them that Edublocks is a tool
# to help them transition from Scratch-like block programming over to text oriented
# Python programming. EduBlocks can become a CRUTCH if they never work with the
# text oriented Python commands, so they will be expected to know how to program
# using text commands only.
#
#
# ========
# Demo #1
# =============================================================
#   "Hello, World!" Program
# =============================================================
'''

# Demo #1

from microbit import *

while True:

    display.scroll("Hello, World!")

    sleep(1000)


'''
# ========
# Demo #2
# ===================================================================
# Simple Microbit/MicroPython "Hello, World!" program modified
# to show the pre-defined HEART image in addition to "Hello, World!"
# ===================================================================
'''

# Demo #2

from microbit import *

while True:

    display.scroll("Hello, World!")    # Use scroll() method to display text

    sleep(1000)

    display.show(Image.HEART)          # Use show() method to display images	

    sleep(1000)


'''
# ========
# Demo #3
# ===================================================================
# Display text strings like "Hello, World!" using "display.scroll()"
# verses "display.show()".
# ===================================================================

# With "display.show()", each letter is suddenly flashed on the display
# without any scrolling. While this may be good for displaying single
# letters or numbers, displaying words with repeating letters will
# look mispelled since there is no display change with the second letter.
# Try it with a word like "Hello". It will look more like "Helo" with
# the "l" letter appearing a tad bit longer (barely noticable).
#
# With "display.scroll()", each letter is scrolled from right to left
# across the 5x5 LED matrix display. Besides fixing the problem with
# being able to view repeating letters, this method makes the text a
# lot easier to read (IMHO).
#
'''

# Demo 3

from microbit import *

while True:

    display.show("Hello, World!")   # Pay attention to "l" in "Hello"...
    sleep(2000)

    display.scroll("Hello, World!")
    sleep(2000)

    display.show("The quick brown fox jumps over the lazy dog.")
    sleep(2000)

    display.scroll("The quick brown fox jumps over the lazy dog.")
    sleep(2000)


'''
# Demo #4
# ===================================================================
# This version of my "Hello, World!" program shows how to use the
# "display.show()" method to display one of some 20+ predefined
# images. These small 5x5 images are more like "emojis".
# ===================================================================

# The "microbit" library includes an object called 'Image' which
# itself is a kind-of library of predefined images. When using these
# named items with the "display.show()" command, be sure NOT to
# enclose the images name within quotes. Named items, be they objects,
# constants or variables must never be enclosed in quotes because they
# are not strings.
#
# Here's a list of predefine images contained within the Image object:
#
# 'HEART', 'HEART_SMALL', 'HAPPY', 'SMILE', 'SAD', 'CONFUSED',
# 'ANGRY', 'ASLEEP', 'SURPRISED', 'SILLY', 'FABULOUS', 'MEH',
# 'YES', 'NO', 'CLOCK12', 'CLOCK1', 'CLOCK2', 'CLOCK3', 'CLOCK4',
# 'CLOCK5', 'CLOCK6', 'CLOCK7', 'CLOCK8', 'CLOCK9', 'CLOCK10',
# 'CLOCK11', 'ARROW_N', 'ARROW_NE', 'ARROW_E', 'ARROW_SE', 'ARROW_S',
# 'ARROW_SW', 'ARROW_W', 'ARROW_NW', 'TRIANGLE', 'TRIANGLE_LEFT',
# 'CHESSBOARD', 'DIAMOND', 'DIAMOND_SMALL', 'SQUARE', 'SQUARE_SMALL',
# 'RABBIT', 'COW', 'MUSIC_CROTCHET', 'MUSIC_QUAVER', 'MUSIC_QUAVERS',
# 'PITCHFORK', 'XMAS', 'PACMAN', 'TARGET', 'ALL_CLOCKS', 'ALL_ARROWS',
# 'TSHIRT', 'ROLLERSKATE', 'DUCK', 'HOUSE', 'TORTOISE', 'BUTTERFLY',
# 'STICKFIGURE', 'GHOST', 'SWORD', 'GIRAFFE', 'SKULL', 'UMBRELLA'
#  and 'SNAKE'.
#
# To use a predefined image, first import the "microbit" library module
# and then use the "display.show()" command as shown in the code below.
# In this program we will alternately display the text string "Hello,
# World!" and the predefined 'HAPPY' image. After getting this program
# to work, feel free to experiment with displaying some of the other
# predefined images.
#
'''

# Demo #4

from microbit import *

while True:
    display.show("Hello, World!")
    sleep(1000)
    display.show(Image.HAPPY)
    sleep(1000)


'''
# For the remainder of the period, let the kids play with writing simple
# programs to view the various pre-defined images files listed above.

# End of Lesson #1.
'''
