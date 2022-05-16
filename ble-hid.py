import machine
# Implements a BLE HID keyboard
import time
from machine import SoftSPI, Pin
from hid_services import Keyboard


# key0 = 0x00
# key1 = 0x00
# key2 = 0x00
# key3 = 0x00


    # Function that catches device status events
def keyboard_state_callback():
    if keyboard.get_state() is Keyboard.DEVICE_IDLE:
        return
    elif keyboard.get_state() is Keyboard.DEVICE_ADVERTISING:
        return
    elif keyboard.get_state() is Keyboard.DEVICE_CONNECTED:
        return
    else:
        return

def keyboard_event_callback(bytes):
    print("Keyboard state callback with bytes: ", bytes)



h_lower_letters = [ ( chr(i),  0, 0x04 + i - ord("a")) for i in range(ord('a'),ord('z')+1) ]
h_upper_letters = [ ( chr(i),  2, 0x04 + i - ord("A")) for i in range(ord('A'),ord('Z')+1) ]
h_numbers = [(str(x), 0, i + 0x1e) for (i,x) in enumerate(list('1234567890'))]
h_above_numbers = list(zip('!@£$%^&*()', [2] * 10, range(0x1e, 0x1e + 10)))
h_lower_symbols = list(zip('\n\x27\b\t -=[]\\§;\'`,./', [0] * 18, range(0x28, 0x28 + 18)))
h_higher_symbols = list(zip('_+{}|±:"~<>?', [2] * 17, range(0x2d, 0x2d + 18 - 5)))

h_keys = h_lower_letters + h_upper_letters + h_numbers + h_above_numbers + h_lower_symbols + h_higher_symbols
s2hids = { c: (mods, code) for (c, mods, code) in h_keys}

def send_char(c):
    mods = 0
#     if char == " ":
#         mod = 0
#         code = 0x2C
#     elif ord("a") <= ord(char) <= ord("z"):
#         mod = 0
#         code = 0x04 + ord(char) - ord("a")
#     elif ord("A") <= ord(char) <= ord("Z"):
#         mod = 1
#         code = 0x04 + ord(char) - ord("A")
#     elif char == '!':
#         bang = True
#         return
    if c in s2hids:
        (mods, code) = s2hids[c]
    else:
        assert 0
#         mod = 0
#         code = 0x04 + ord(char)
            
    #         assert 0

    keyboard.set_keys(code)
    keyboard.modifiers = mods
#     keyboard.set_modifiers(left_shift=mod)
    keyboard.notify_hid_report()
    time.sleep_ms(2)

    keyboard.set_keys()
    keyboard.set_modifiers()
    keyboard.notify_hid_report()
    time.sleep_ms(2)


def send_string(st):
    for c in st:
        send_char(c)
        time.sleep_ms(20)


# Test routine
def test():
    time.sleep(5)
    keyboard.set_battery_level(50)
    keyboard.notify_battery_level()
    time.sleep_ms(2)



    send_string(" Hello World\n")

    keyboard.set_battery_level(100)
    keyboard.notify_battery_level()

    # if __name__ == "__main__":

# Create our device
keyboard = Keyboard("Keyboard")
# Set a callback function to catch changes of device state
keyboard.set_state_change_callback(keyboard_state_callback)
# Start our device
keyboard.start()

   # Main loop
# def connect():
# line = None

def start():
    while True:


        # If the variables changed do something depending on the device state
#         if (key0 != 0x00) or (key1 != 0x00) or (key2 != 0x00) or (key3 != 0x00):
            # If connected set keys and notify
            # If idle start advertising for 30s or until connected
            
        if keyboard.get_state() is Keyboard.DEVICE_CONNECTED:
            return()
#             keyboard.set_keys(key0, key1, key2, key3)
#             keyboard.notify_hid_report()
#             send_string(" Hello World")
#             time.sleep(1000)
        elif keyboard.get_state() is Keyboard.DEVICE_IDLE:
            keyboard.start_advertising()
            i = 10
            while i > 0 and keyboard.get_state() is Keyboard.DEVICE_ADVERTISING:
                time.sleep(3)
                i -= 1
            if keyboard.get_state() is Keyboard.DEVICE_ADVERTISING:
                keyboard.stop_advertising()

        if keyboard.get_state() is Keyboard.DEVICE_CONNECTED:
            time.sleep_ms(20)
        else:
            time.sleep(2)
            
            
# start()
#####################

# f = open('bruce.sql', 'r')

def send_file():
#     time.sleep(3000)
    with open('example.txt') as f:
        line = f.readline()
        while line:
            line = f.readline().replace('\t', '  ')
            send_string(line)
            
            
#         print(line)
        
