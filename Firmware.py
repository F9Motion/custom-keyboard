# Now we write code
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard=Keyboard(usb_hid.devices)
ROW_GPIOS = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11
]

COL_GPIOS = [
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16,
    board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22
]

rows = []
for pin in ROW_GPIOS:
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.INPUT
    io.pull = digitalio.Pull.DOWN
    rows.append(io)
cols = []
for pin in COL_GPIOS:
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.OUTPUT
    io.value = False
    cols.append(io)

KEYMAP = [
    #ROW0
    [Keycode.ESCAPE, Keycode.F1, Keycode.F2, Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6, Keycode.F7, Keycode.F8, Keycode.F9, Keycode.F10],
    #ROW1
    [Keycode.GRAVE, Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR, Keycode.FIVE, Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT, Keycode.NINE, Keycode.ZERO],
    #ROW2
    [Keycode.TAB, Keycode.Q, Keycode.W, Keycode.E, Keycode.R, Keycode.T, Keycode.Y, Keycode.U, Keycode.I, Keycode.O, Keycode.P],
    #ROW3
    [Keycode.CAPS_LOCK, Keycode.A, Keycode.S, Keycode.D, Keycode.F, Keycode.G, Keycode.H, Keycode.J, Keycode.K, Keycode.L, Keycode.SEMICOLON],
    #ROW4
    [Keycode.LEFT_SHIFT, Keycode.Z, Keycode.X, Keycode.C, Keycode.V, Keycode.B, Keycode.N, Keycode.M, Keycode.COMMA, Keycode.PERIOD, Keycode.FORWARD_SLASH],
    #ROW5
    [Keycode.LEFT_CONTROL, Keycode.LEFT_GUI, Keycode.LEFT_ALT, Keycode.SPACE, Keycode.RIGHT_ALT, Keycode.RIGHT_GUI, None, Keycode.RIGHT_CONTROL, None, None, None],
    #ROW6
    [None, None, None, None, None, None, None, Keycode.F12, Keycode.F11, None, None],
    #ROW7
    [Keycode.KEYPAD_MINUS, Keycode.KEYPAD_ASTERISK, Keycode.KEYPAD_FORWARD_SLASH, Keycode.KEYPAD_NUMLOCK, Keycode.PAGE_UP, Keycode.HOME, Keycode.INSERT, Keycode.BACKSPACE, Keycode.EQUALS, Keycode.MINUS, None],
    #ROW8
    [Keycode.KEYPAD_PLUS, Keycode.KEYPAD_NINE, Keycode.KEYPAD_EIGHT, Keycode.KEYPAD_SEVEN, Keycode.PAGE_DOWN, Keycode.END, Keycode.DELETE, Keycode.ENTER, Keycode.RIGHT_BRACKET, Keycode.LEFT_BRACKET, None],
    #ROW9
    [Keycode.KEYPAD_SIX, Keycode.KEYPAD_FIVE, Keycode.KEYPAD_FOUR, Keycode.ENTER, Keycode.QUOTE, None, None, None, None, None, None],
    #ROW10
    [Keycode.ENTER, Keycode.KEYPAD_THREE, Keycode.KEYPAD_TWO, Keycode.KEYPAD_ONE, Keycode.UP_ARROW, Keycode.RIGHT_SHIFT, None, None, None, None, None],
    #ROW11
    [Keycode.KEYPAD_PERIOD, Keycode.KEYPAD_ZERO, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, None, None, None, None, None, None,]
]

currently_pressed = set()

while True:
    new_pressed = set()
    for col_idx, col_pin in enumerate(cols):
        col_pin.value = True
        time.sleep(0.0001)
        for row_idx, row_pin in enumerate(rows):
            if row_pin.value:
                key = KEYMAP[row_idx][col_idx]
                if key is not None:
                    new_pressed.add(key)
        col_pin.value = False
    for key in new_pressed - currently_pressed:
        keyboard.press(key)
    for key in currently_pressed - new_pressed:
        keyboard.release(key)

    currently_pressed = new_pressed
    time.sleep(0.005)

