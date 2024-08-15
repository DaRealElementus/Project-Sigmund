from gpiozero import Servo
from time import sleep, time

# Define a map function similar to Arduino's
def map_val(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Servo setup
myServo1 = Servo(11)
myServo2 = Servo(10)
myServo3 = Servo(9)
myServo4 = Servo(8)

x_direction = 0
y_direction = 0
blinkinterval = 0

def setup():
    # Setup code for Raspberry Pi
    myServo1.value = None
    myServo2.value = None
    myServo3.value = None
    myServo4.value = None

def loop():
    global blinkinterval
    global x_direction
    global y_direction
    while True:
        # Replace these values with actual sensor readings
        x_pos = 512  # Example placeholder value
        y_pos = 512  # Example placeholder value

        # Map x_pos and y_pos values to servo range (assume -1 to 1 for gpiozero Servo)
        x_direction = map_val(x_pos, 0, 1023, -1, 1)
        y_direction = map_val(y_pos, 0, 1023, -1, 1)

        lr_direction()
        ud_direction()

        if (time() - blinkinterval) > 3.2:  # Converted milliseconds to seconds
            blink()

        sleep(0.1)  # Add some delay for stability

def blink():
    # Assuming the values for blinking are set to specific angles
    myServo3.value = 0.5
    myServo4.value = -0.5
    sleep(0.5)  # Small delay to simulate blink
    myServo3.value = -0.5
    myServo4.value = 0.5
    sleep(0.5)  # Small delay to simulate blink

def lr_direction():
    myServo1.value = x_direction

def ud_direction():
    myServo2.value = y_direction

if __name__ == '__main__':
    setup()
    loop()
