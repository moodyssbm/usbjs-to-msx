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
            1: 'LEFT-Y'
        }
        self.buttonNames = {
            1:  'A',
            2:  'B'
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

    # Determine the type
    if eventType == 'BUTTON':
        if control == 'A':
            if value == True:
                GPIO.output(msx.BA, GPIO.HIGH)
            else:
                GPIO.output(msx.BA, GPIO.LOW)
        if control == 'B':
            if value == True:
                GPIO.output(msx.BB, GPIO.HIGH)
            else:
                GPIO.output(msx.BB, GPIO.LOW)

    # X1 = Right, Y1 = down
    elif eventType == 'AXIS':
        if control == 'LEFT-X':
            if value == 1.0:
                GPIO.output(msx.LF, GPIO.LOW)
                GPIO.output(msx.RT, GPIO.HIGH)
            elif value == -1.0:
                GPIO.output(msx.RT, GPIO.LOW)
                GPIO.output(msx.LF, GPIO.HIGH)
            else:
                GPIO.output(msx.RT, GPIO.LOW)
                GPIO.output(msx.LF, GPIO.LOW)
        elif control == 'LEFT-Y':
            if value == 1.0:
                GPIO.output(msx.UP, GPIO.LOW)
                GPIO.output(msx.DN, GPIO.HIGH)
            elif value == -1.0:
                GPIO.output(msx.DN, GPIO.LOW)
                GPIO.output(msx.UP, GPIO.HIGH)
            else:
                GPIO.output(msx.DN, GPIO.LOW)
                GPIO.output(msx.UP, GPIO.LOW)

