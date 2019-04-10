# A minimal 'scrollbit' library module

from microbit import sleep, i2c, Image

WIDTH = 17
HEIGHT = 7

orientation = 0
NORMAL = 0
INVERT = 1

_ADDRESS = 0x74

_MODE_REGISTER = 0x00
_FRAME_REGISTER = 0x01
_AUDIOSYNC_REGISTER = 0x06
_SHUTDOWN_REGISTER = 0x0a

_CONFIG_BANK = 0x0b
_BANK_ADDRESS = 0xfd

_PICTURE_MODE = 0x00
_AUTOPLAY_MODE = 0x08
_AUDIOPLAY_MODE = 0x18

_ENABLE_OFFSET = 0x00
_BLINK_OFFSET = 0x12
_COLOR_OFFSET = 0x24

_frame = 0
_buf = bytearray(145)
_icons = [getattr(Image,x) for x in dir(Image) if hasattr(getattr(Image,x),'get_pixel')]

def _i2c_write(*args):
    if len(args) == 1: args = args[0]
    i2c.write(_ADDRESS, bytes(args))

def clear():
    global _buf
    del _buf
    _buf = bytearray(145)

def show():
    global _frame

    _frame = not _frame

    _i2c_write(_BANK_ADDRESS, _frame)

    _buf[0] = _COLOR_OFFSET
    _i2c_write(_buf)

    _i2c_write(_BANK_ADDRESS, _CONFIG_BANK)
    _i2c_write(_FRAME_REGISTER, _frame)

def set_pixel(col, row, brightness):
    _buf[_pixel_addr(col, row)] = brightness

def get_pixel(col, row):
    return _buf[_pixel_addr(col, row)]

def _pixel_addr(x, y):
    y =  (7 - (y + 1))*(1 - orientation) + orientation*y
    x = (17 - (x + 1))*orientation + (1 - orientation)*x

    if x > 8:
        x = x - 8
        y = 6 - (y + 8)
    else:
        x = 8 - x

    return (x * 16 + y) + 1

_i2c_write(_BANK_ADDRESS, _CONFIG_BANK)

sleep(100)
_i2c_write(_SHUTDOWN_REGISTER, 0)
sleep(100)
_i2c_write(_SHUTDOWN_REGISTER, 1)
sleep(100)

_i2c_write(_MODE_REGISTER, _PICTURE_MODE)
_i2c_write(_AUDIOSYNC_REGISTER, 0)

for bank in [1,0]:
    _i2c_write(_BANK_ADDRESS, bank)
    _i2c_write([0] + [255] * 17)

clear()
show()
