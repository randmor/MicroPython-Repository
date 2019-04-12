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

# EOF
