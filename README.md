Here are several versions of my "Simple Pong Game" for various configurations of the BBC Micro:bit board.

A.) The basic version is "mpSimplePong1.py" which runs on the plain old vanilla Microbit with its 5x5 red LED display.

B.) Two versions of my Simple Pong Game for the Micro:bit/Micro:Pixel Hardware Combo.

    The ProtoPic Micro:Pixel 4x8 NeoPixel display board provides the Micro:bit with an interesting color display option.
    For more info on this display, check out this URL:
    
         https://www.proto-pic.co.uk/micropixel-4x8-ws2812b-board-for-bbc-microbit.html

    1.) The first version of my game is pretty much "msSimplePong1.py" re-written (ported) over to the Micro:Pixel display 
    which relies on the MicroPython "neopixel" library plus a couple of x,y coordinate plot functions: 

        1.) "npPlot1()", for plotting points (NeoPixel LEDs) when the board combo is held in "landscape" orientation; and 
    
        2.) "npPlot2()", for plotting points (NeoPixel LEDs) when the board combo is held in "potrait" orientation.

    Also, since the Micro:bit board plugs into the Micro:Pixel board such that the two displays are on opposite sides, when you 
    go to hold the board combo such that the MicroPixel display is up, the MicroPixel's accelerometer is upside down, so I had 
    to rewrite some of the code to compensate for this now upside down accelerometer.
    
    2.) The second version of my Simple Pong Game for the Micro:bit/Micro:Pix hardware combo adds music and sound effects. 
    To be able to hear the music and sound effects, you have to add an external speaker to Micro:bit "pin0", and then make  
    a "cut and jump" operation on the Micro:Pixel board (there are pads designed to allow you to do this on thier board and 
    instructions on how to do it on their web page that describes the "micro:pixel" board). As a result of this operation, 
    the 4x8 NeoPixel display is controlled via Micro:bit "pin8". So, in the code, we create an instance of our neoPixel object
    class using this command: "np = neopixel.NeoPixel(pin8, 32)". That's "pin8" instead of "pin0".
    
C.) A version of my Simple Pong Game for the Micro:bit/Scroll:bit Hardware Combo.

    The Pimoroni "Scroll:bit" display board provides the Micro:bit with a much larger 7x17 white LED display option.
    For more info on this display, check out this URL:    
    
        https://shop.pimoroni.com/products/scroll-bit
    
    I have this version working will upload it here later today.
    
    I like the fact that the Pimoroni design adds the new dislay to the same side of the Micro:bit board as its 5x5 red LED 
    display so you can use the both displays at the same time, maybe the 5x5 display for text messages and emojis, and the 
    7x17 display as your gameboard.  Also, it does not cover up the Reset button on the backside of the Micro:bit board as 
    happens when you use the Proto-PIC boad. [Maybe Proto-PIC can do a Rev 2 of their Micro:Pixel board to use the Pimoroni 
    layout design which would also make using the accelerometer easier to program. Just a suggestion.]
    
    At first my impresion of the Scroll:bit was soured because I found it hard to distinguish between different levels of 
    light intensity (something important to have when all your game elements are all the same colored pixels. It's relatively 
    easy on the Micro:bit's 5x5 red LED display which only has 10 levels (the Scroll:bit has 256 brightness levels). I was able
    to resolve this by limiting myself to 7 brightness levels: # Define 7 brightness levels with this statement:
    
        brightness = [0, 5, 10, 20, 40, 80, 160]
    
    Then in my game, the paddle is 40 (brightness[4]) and the ball is 10 (brightness[2]). This allows me a fairly good level
    of distinguishability, especially for an "indoors game". Outdoors, or under bright lights, you may need to increase the 
    brightness (and this is true for all my games... I develop them in a rather low light setting at my home).
    
    
    
    
    Micro:bit's 
