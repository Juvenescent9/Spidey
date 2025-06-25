from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
import board

# Initialize KMK keyboard
keyboard = KMKKeyboard()

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)


# COLUMN pins (wired to cathode side of diodes)
keyboard.col_pins = (board.GP3, board.GP4, board.GP2)

keyboard.row_pins = (board.GP26, board.GP27, board.GP28)

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)




keyboard.extensions.append(MediaKeys())

# 3×3 key layout:
keyboard.keymap = [
    [KC.ESC,  KC.VOLU, KC.VOLD,    # Top row
     KC.PWR,  KC.SLEP, KC.WAKE,    # Middle row
     KC.F4,   KC.PSCR, KC.PRNT]    # Bottom row
]

if __name__ == '__main__':
    keyboard.go()
