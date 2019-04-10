Here are several versions of my "Simple Pong Game" for various configurations of the BBC Micro:bit board.

A.) The basic version is "mpSimplePong1.py" which runs on the plain old Microbit with its 5x5 red LED display.

B.) Two versions of my Simple Pong Game for the Micro:bit/Micro:Pixel Hardware Combo.

    The Proto-PIC Micro:Pixel 4x8 NeoPixel display board provides the Micro:bit with an interesting color 
    display option. For more info on this display, check out this URL:
    
         https://www.proto-pic.co.uk/micropixel-4x8-ws2812b-board-for-bbc-microbit.html

    1.) The first version of my pong game is pretty much "msSimplePong1.py" re-written to run on the 
    Micro:Pixel display, which relies on the MicroPython "neopixel" library plus a couple of x,y 
    coordinate plot functions: 

        1.) "npPlot1()", for plotting points (NeoPixel LEDs) when the board combo is held in 
        "landscape" orientation; and 
    
        2.) "npPlot2()", for plotting points (NeoPixel LEDs) when the board combo is held in 
        "portrait" orientation.

    Also, since the Micro:bit board plugs into the Micro:Pixel board such that the two displays are on 
    opposite sides. So, when you go to hold this board combo such that the Micro:Pixel display is up, 
    the Micro:bit's accelerometer is upside-down. This means I had to rewrite some of the code to 
    compensate for this now upside-down accelerometer.
    
    2.) The second version of my Simple Pong Game for the Micro:bit/Micro:Pixel hardware combo adds music 
    and sound effects. To be able to hear the music and sound effects, you have to add an external speaker 
    to Micro:bit "pin0", and then make a "cut and jump" operation on the Micro:Pixel board (there are pads 
    designed to allow you to do this on their board and instructions on how to do it on their web page 
    that describes the "micro:pixel" board). As a result of this operation, the 4x8 NeoPixel display is 
    now controlled via Micro:bit "pin8". So, in the code, we create an instance of our neopixel object
    class using this command: "np = neopixel.NeoPixel(pin8, 32)". That's "pin8" instead of "pin0".
    
C.) A version of my Simple Pong Game for the Micro:bit/Scroll:bit Hardware Combo.

    The Pimoroni "Scroll:bit" display board provides the Micro:bit with a much larger 7x17 low-power white 
    LED display option. For more info on this display, check out this URL:    
    
        https://shop.pimoroni.com/products/scroll-bit
    
    I have this version working will upload it here later today.
    
    I like the fact that the Pimoroni design adds the new display to the same side of the Micro:bit 
    board as its 5x5 red LED display. This allows you to write programs that use both displays at 
    the same time (i.e. without having to constantly flip the board combo over and back again). In 
    my game, I use the 5x5 display for sending messages (like the score) and emojis (e.g. "happy face" 
    when you score a point, "sad face" when you loose a point). That frees up the 7x17 display to be 
    used for our "gameboard". 
    
    Also, the Pimoroni Scroll:bit design does not cover up the Micro:bit's Reset button. This is a 
    sometimes frustrating "feature" of the Proto-PIC design: inaccessibility of the reset button. 
    [Maybe the Proto-PIC folks can do a "Rev 2" of their Micro:Pixel board to use the Pimoroni layout 
    design which would also make using the accelerometer easier to program. I did NOT have any such 
    "accelerometer disorientation problems" with the Scroll:bit.]
    
    But, at first, my impression of the Scroll:bit was soured because I found it hard to distinguish 
    between different levels of light intensity. Ease of LED distinguishability is something important 
    to have when all your game elements (e.g. the good guy, the bad guy, the ball (or bomb), and any 
    obstacles) are all single monochrome LEDs. On the Micro:bit 5x5 red LED display, it's relatively 
    easy to distinguish between things based on 10 different LED brightness levels. But on the Scroll:bit,
    with its 256 different brightness levels, it's much more of a challenge. After some experimenting
    I have settled on 7 brightness levels as shown in the following Python statement:
    
        brightness = [0, 5, 10, 20, 40, 80, 160]
    
    So, in my pong game, the paddle is 40 (brightness[4]) and the ball is 10 (brightness[2]). This allows 
    me a fairly good level of distinguishability, especially for an "indoors game". Outdoors, or under 
    bright lights, you may need to increase the brightness of the LED pixels. This is generally true for
    most of my games, as I develop them in rather low-light conditions at my home.

# EOF
