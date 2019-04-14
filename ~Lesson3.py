'''
#
# Lesson #3: The Microbit's Built-In 3-Axes Accelerometer
#
# This file contains the source code to several MicroPython demo programs to be
# used in this third lesson. It also contains much of the lesson plan.
#
#
# Part 1: Overview of the Microbit's Accelerometer
#
# The 3-axes accelerometer on the Microbit board provides the capability of sensing
# the position of the Microbit when held in 3D (three dimensional) space. You have 
# seen this in the iPhone, iPad and similar devices where you can turn a picture (or
# a program's user interface) from "landscape" view to "portrait" view and back just 
# by moving the device around in 3D space. What allows this to happen is the 3-axes 
# accelerometer built into the iPad (or similar device) along with the appropriate 
# software. In this class, we will explore how to program the Microbit such that it 
# can detect certain gestures, and depending on the gesture, do a different set of 
# actions.
#
# The low level software support for the Microbit's accelerometer is included in 
# the "microbit" library module where the "accelerometer" is defined as an object with
# its own set of functions (called "methods"). We can view the "accelerometer" object 
# and its associated methods by using the Mu Editor's REPL feature. Here's a sample
# session:

    MicroPython v1.9.2-34-gd64154c73 on 2017-09-01; micro:bit v1.0.1 with nRF51822
    Type "help()" for more information.
    >>> import microbit
    >>> dir(microbit)
    ['__name__', 'Image', 'display', 'button_a', 'button_b', 'accelerometer', 'compass', 
    'i2c', 'uart', 'spi', 'reset', 'sleep', 'running_time', 'panic', 'temperature', 
    'pin0', 'pin1', 'pin2', 'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 
    'pin10', 'pin11', 'pin12', 'pin13', 'pin14', 'pin15', 'pin16', 'pin19', 'pin20']
    >>> dir(accelerometer)
    ['get_x', 'get_y', 'get_z', 'get_values', 'current_gesture', 'is_gesture', 
    'was_gesture', 'get_gestures']
    >>> 

# So, in the sample REPL session (above), we must first import the "microbit" library
# before we can use the "dir(microbit)" command to view what resources are provided in 
# this library module. You should recognize some of these objects including display, 
# Image, button_a, button_b and the sleep() function. You will also see the object 
# named "accelerometer". This object has its own set of functions (methods) which we 
# can view using the "dir(accelerometer)" REPL command. These accelerometer methods
# include:
#
#	accelerometer.get_x()
#	accelerometer.get_y()
#	accelerometer.get_z()
#	accelerometer.get_values()
#	accelerometer.current_gesture()
#	accelerometer.is_gesture()
#	accelerometer.was_gesture()
#	accelerometer.get_gestures()
#
# The first four of these methods deal with raw accelerometer data while the second
# set of four methods involve something called "gestures", which we will talk more 
# about in a few minutes. For now, know that you can get more information on what these 
# methods are and how to use them by searching and reading the Microbit/MicroPython 
# "Read-The-Docs" webpages at this URL:
#
#     https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html
#
# When programming with the raw accelerometer data, know that the x-axis is the axis 
# you want to use if you want your program to respond to "left tilt" or "right tilt", 
# while the y-axis is the axis you want to use to respond to "up tilt" or "down tilt".
# When holding the Microbit so that you can read the 5x5 red LED display, "up" is the 
# side of the Microbit with the micro-USB connector, and when this micro-USB connector 
# rises above the horizontal plane, we have an "up tilt". But, when the micro-USB 
# connector falls below the horizontal plane, we have a "down tilt".
#
# The raw data being returned by the Microbit board generally ranges from -1024 to +1024,
# and that a "level" Microbit will return values near zero for both axes. The "right tilt"
# and the "down tilt" gestures will have positive return values from the "get_x()" and 
# "get_y()" methods, while the "left tilt" and "up tilt" will have negative return values
# from "get_x()" and "get_y()" methods. As with similar devices, the Microbit's z-axis is 
# used to determine if the board is "facing up" or is "facing down". 
# 
# When dealing with the raw data, you will need to arbitraily set some limits between what 
# is "level" and when the board has been tilted. These limits may be "+/-128", "+/-256" or 
# "+/-512" (or anything you feel is right for your application). The magnitude of these 
# limits is something I call "gesture sensitivity". As an example, for a "pong game", you 
# may choose the limit "+/-128". This means the board is more or less level between -127 
# to + 127. But suddenly, at -128, the board is now "tilted-left" (or "tilted-up", depending 
# on the axis you are testing in code). Then at +128, the board suddenly changes from "level" 
# to "tilted-right (or "titled down"). As you can see, programming with the raw data is 
# pretty complicated, but it allows you better control over the accelerometer, depending 
# upon the needs of your application.
#
#
# Part 2: Gestures and the Microbit's 3-Axes Accelerometer
#
# To make programming with the Accelerometer easier (as compared to using raw data), the 
# designers of the Microbit have come up with a set of pre-defined gestures (i.e. ways of 
# moving the Microbit) so that you can write a program that reacts to these gestures rather 
# than having to use the raw accelerometer data. As we saw in the section above, using the 
# raw accelerometer data can be quite confusing. In this part of the lesson we will be 
# studying just the 7 most often used (most useful) gestures: "shake", "up", "down", 
# "left", "right", "face-up" and "face-down".
#
# As a simple example of how to use accelerometer's "shake" gestures, consider the 
# following demo program commonly called "Magic 8 Ball":

'''

#
# Lesson #3, Demo Program #1: The "Magic 8 Ball" game
#
# In this game, think up a question that you would like the answer for
# and then "shake" the Microbit board to see its answer. Notice how 
# the program keeps the text responses in a Python list structure
# commonly called an "array" in other programming languages. The 
# random.choice() method is used to randomly choose a response from
# this array (Python list). The random functions are all kept in the
# "random" library module which must be imported separately.

from microbit import *
import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it"
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"]

while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))

'''
#
# Part 3:
#
# As a second example that uses more of the accelerometer gestures, give
# the following demo program a try:

'''

#
# Lesson #3, Demo Program #2:
#
# Tilt Microbit "face up" for a "happy face" or "face down" for an "angry face".
# Otherwise, display a "surprised face". Notice how far you have to tilt the 
# Microbit over to get an "angry face". 
#

from microbit import *
while True:

    # Assign the current accelerometer gesture to a variable 
    # so if can be later tested.
    gesture = accelerometer.current_gesture()

    # Test "gesture" variable for "face up" or "face down" gestures 
    # and respond appropriately.
    if gesture == "face up":
        display.show(Image.HAPPY)
    elif gesture == "face down":
        display.show(Image.ANGRY)
    else:
        display.show(Image.SURPRISED)

'''
#
# Part 4:
#
# For Lesson 3, Exercise 1, I will give you a set of 6 design criteria 
# and you will write a program that does the job. Be sure to give the 
# students time to figure this program out for themselves. Go around 
# and answer questions and give help as needed.

'''
	1.) Have your program display the "happy face" by default.

	2.) If a "shake" gesture is detected, have your program 
	    display an "angry face".

	3.) If a "right" gesture is detected, display the letter "R".

	4.) If a "left" gesture is detected, display the letter "L".

	5.) If a "up" gesture is detected, display the letter "U".

	6.) If a "down" gesture is detected, display the letter "D".

'''
#
# For my solution to Exercise 1 (above), see the file "accelTest1.py" 
# on my GitHub webpage.
#
#
# Part 5:
#
# Another use for the accelerometer is as a motion detector that could
# be used to set off an alarm. In the next demo program we will use the
# accelerometer.get_z() method to first provide a baseline z-axis
# measurement, and then once the alarm has been armed, it will run in 
# a loop testing the z-axis value to see if there has been a significant 
# change. If so, it will turn on an alarm that provides both an audible 
# and a visual alarm. To hear the audible alarm you will need to hook
# up an external speaker between Microbit pins "0" and "GND". The visual
# alarm indicator will be that the "happy face" has turned into an "angry
# face".
#
# Play with the code until you understand how it works.
#
#
'''
# Lesson #3, Demo Program #3: A Simple Alarm Program. 
#
# Press button "A" to arm the alarm.
# Press button "B" to turn off the alarm
#
# Program uses acclerometer.get_z() method to detect any 
# movement of the Microbit board. If movement is detected,
# it sounds an alarm and displays a big "X" on the LED display.
#
# Program also uses the music.pitch() method to make a simple
# audible alarm sound in addition to displaying the angry face. 
# To hear the alarm, connect a speaker between Microbit pin "0"
# and the pin marked "GND".
#
# Filename: "simpleAlarmProgram.py"

from microbit import *
import music

def soundAlarm():
    for i in range(0, 4):
        music.pitch(freq * i, 100)
        display.show(Image.ANGRY)

freq = 1000
alarmArmed = False
alarmOn = False

while True:
    display.show("A")   # Press "A" button to arm the alarm
    if button_a.is_pressed():
        z = accelerometer.get_z()      # Take a z-axis reading while Microbit is still
        display.scroll("z=" + str(z))  # Just a test / It displays something btw -1008 to -1024
        alarmArmed = True
        display.show(Image.TARGET)
        
    while alarmArmed:
	display.show(Image.HAPPY)
        if accelerometer.get_z() < z - 30:
            alarmOn = True
        while alarmOn:   
            soundAlarm()    
            if button_b.is_pressed():
                alarmOn = False
                alarmArmed = False
                display.clear()   
    	    sleep(100)
        sleep(100)    
'''
# EOF
