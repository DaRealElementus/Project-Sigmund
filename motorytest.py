import time
import asyncio
import pigpio
import RPi.GPIO as GPIO 
from decibeltest import *


#yk you can use PWM For the RGB right? which removes the need for RPi.GPIO, thus reducing lag and making our program more efficient


# Define a map function similar to Arduino's
def map_val(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Initialize pigpio and define the GPIO pins for the servos
pi = pigpio.pi()
SERVO_PIN1 = 17  # GPIO17 (Pin 11)
SERVO_PIN2 = 27  # GPIO27 (Pin 13)
SERVO_PIN3 = 22  # GPIO22 (Pin 15)
SERVO_PIN4 = 23  # GPIO23 (Pin 16)

x_direction = 0
y_direction = 0
blinkinterval = time.time()  # Initialize with current time

emotion = "IDK"

# RGB LED Pin Definitions
redPin = 12
greenPin = 19
bluePin = 13

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

def set_white():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)

def set_blue():
    GPIO.output(redPin, GPIO.HIGH)
    GPIO.output(greenPin, GPIO.HIGH)
    GPIO.output(bluePin, GPIO.LOW)

def set_yellow():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.HIGH)

def set_light_blue():
    GPIO.output(redPin, GPIO.HIGH)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)

def set_purple():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.HIGH)
    GPIO.output(bluePin, GPIO.LOW)

def setup():
    # Setup code for Raspberry Pi
    pi.set_servo_pulsewidth(SERVO_PIN1, 0)
    pi.set_servo_pulsewidth(SERVO_PIN2, 0)
    pi.set_servo_pulsewidth(SERVO_PIN3, 0)
    pi.set_servo_pulsewidth(SERVO_PIN4, 0)

async def loop():
    global blinkinterval
    global x_direction
    global y_direction
    while True:
        # Replace these values with actual sensor readings
        x_pos = x_difference
        # y_pos = 512

        # Map x_pos and y_pos values to servo pulse width range (500 to 2500 microseconds)
        x_direction = map_val(x_pos, 0, 1023, 500, 2500)
        # y_direction = map_val(y_pos, 0, 1023, 500, 2500)

        lr_direction()
        # ud_direction()

        if (time.time() - blinkinterval) > 3.2:  # Converted milliseconds to seconds
            await blink()
            blinkinterval = time.time()  # Update blink interval time

        #Change RGB LED color based on emotion
        if emotion == "Happy":
            set_yellow
        if emotion == "Sad":
            set_blue
        if emotion == "Shocked":
            set_white
        if emotion == "Understanding":
            set_light_blue
        if emotion == "Concerned":
            set_purple
        await asyncio.sleep(0.1)

async def blink():
    # Assuming the values for blinking are set to specific pulse widths
    pi.set_servo_pulsewidth(SERVO_PIN3, 2000)
    pi.set_servo_pulsewidth(SERVO_PIN4, 1000)
    await asyncio.sleep(0.5)
    pi.set_servo_pulsewidth(SERVO_PIN3, 1000)
    pi.set_servo_pulsewidth(SERVO_PIN4, 2000)
    await asyncio.sleep(0.5)

def lr_direction():
    pi.set_servo_pulsewidth(SERVO_PIN1, x_direction)

def ud_direction():
    pi.set_servo_pulsewidth(SERVO_PIN2, y_direction)

if __name__ == '__main__':
    setup()
    try:
        asyncio.run(loop())  # Start the asyncio event loop
    finally:
        GPIO.cleanup()  # Clean up GPIO on exit
