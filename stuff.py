import machine

# machine.freq(240000000)
# 
# from machine import Pin
# 
# print('Frequency: %s' % machine.freq())

# pled = Pin(2, Pin.OUT)    # create output pin on GPIO0
# pled.on()                 # set pin to "on" (high) level
# pled.off()                # set pin to "off" (low) level

h_lower_letters = [ ( chr(i),  0, 0x04 + i - ord("a")) for i in range(ord('a'),ord('z')+1) ]
h_upper_letters = [ ( chr(i),  2, 0x04 + i - ord("A")) for i in range(ord('A'),ord('Z')+1) ]
h_numbers = [(str(x), 0, i + 0x1e) for (i,x) in enumerate(list('1234567890'))]
h_above_numbers = list(zip('!@£$%^&*()', [2] * 10, range(0x1e, 0x1e + 10)))
h_lower_symbols = list(zip('\n\x27\b\t -=[]\\§;\'`,./', [0] * 18, range(0x28, 0x28 + 18)))
h_higher_symbols = list(zip('_+{}|±:"~<>?', [2] * 17, range(0x2d, 0x2d + 18 - 5)))

h_keys = h_lower_letters + h_upper_letters + h_numbers + h_above_numbers + h_lower_symbols + h_higher_symbols
s2hids = { c: (mods, code) for (c, mods, code) in h_keys}

'ENTER': 0x28,  # // Keyboard Return (ENTER)
'ESC': 0x29,  # // Keyboard ESCAPE
'BACKSPACE': 0x2a,  # // Keyboard DELETE (Backspace)
'TAB': 0x2b,  # // Keyboard Tab
'SPACE': 0x2c,  # // Keyboard Spacebar
'MINUS': 0x2d,  # // Keyboard - and _
'EQUAL': 0x2e,  # // Keyboard = and +
'LEFTBRACE': 0x2f,  # // Keyboard [ and {
'RIGHTBRACE': 0x30,  # // Keyboard ] and }
'BACKSLASH': 0x31,  # // Keyboard \ and |
'HASHTILDE': 0x32,  # // Keyboard Non-US # and ~
'SEMICOLON': 0x33,  # // Keyboard ; and :
'APOSTROPHE': 0x34,  # // Keyboard ' and "
'GRAVE': 0x35,  # // Keyboard ` and ~
'COMMA': 0x36,  # // Keyboard , and <
'DOT': 0x37,  # // Keyboard . and >
'SLASH': 0x38,  # // Keyboard / and ?
'CAPSLOCK': 0x39,  # // Keyboard Caps Lock
# numbers = [[str(x), 0, i + 0x1e] for (i,x) in enumerate(rotate(list(range(10)),1))]
# above_numbers = [[str(x), 0, i + 0x1e] for (i,x) in enumerate(list('!@£$%^&*()'))]

def rotate(l, n):
    return l[n:] + l[:n]

'1': 0x1e,  # // Keyboard 1 and !
'2': 0x1f,  # // Keyboard 2 and @
'3': 0x20,  # // Keyboard 3 and #
'4': 0x21,  # // Keyboard 4 and $
'5': 0x22,  # // Keyboard 5 and %
'6': 0x23,  # // Keyboard 6 and ^
'7': 0x24,  # // Keyboard 7 and &
'8': 0x25,  # // Keyboard 8 and *
'9': 0x26,  # // Keyboard 9 and (
'0': 0x27,  # // Keyboard 0 and )

