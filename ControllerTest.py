import RPi.GPIO as GPIO
import Gamepad
import time
import MSXPins as msx

# Preconfigure GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(msx.UP, GPIO.OUT)    # Up
GPIO.setup(msx.DN, GPIO.OUT)    # Down
GPIO.setup(msx.LF, GPIO.OUT)    # Left
GPIO.setup(msx.RT, GPIO.OUT)    # Right
GPIO.setup(msx.BA, GPIO.OUT)    # Button A
GPIO.setup(msx.BB, GPIO.OUT)    # Button B

# Make our own custom gamepad
# The numbers can be figured out by running the Gamepad script:
# ./Gamepad.py
# Press ENTER without typing a name to get raw numbers for each
# button press or axis movement, press CTRL+C when done
class CustomGamepad(Gamepad.Gamepad):
    def __init__(self, joystickNumber = 0):
        Gamepad.Gamepad.__init__(self, joystickNumber)
        self.axisNames = {
            0: 'LEFT-X',
            1: 'LEFT-Y',
            2: 'RIGHT-Y',
            3: 'RIGHT-X',
            4: 'DPAD-X',
            5: 'DPAD-Y'
        }
        self.buttonNames = {
            0:  'X',
            1:  'A',
            2:  'B',
            3:  'Y',
            4:  'ZL',
            5:  'ZR',
            6:  'L',
            7:  'R',
            8:  'SELECT',
            9:  'START',
            10: 'L3',
            11: 'R3'
        }
        self._setupReverseMaps()

# Gamepad settings
gamepadType = CustomGamepad

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Main loop
while gamepad.isConnected():
    # Wait for the next event
    eventType, control, value = gamepad.getNextEvent()

    print(control)
    print(value)

