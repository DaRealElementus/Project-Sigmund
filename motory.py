from gpiozero import Servo
from time import sleep, time

# Define a map function similar to Arduino's
def map_val(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Servo setup
myServo1 = Servo(11) #X value
myServo2 = Servo(10) #Y value
myServo3 = Servo(9)  #blink servo?
myServo4 = Servo(8)  #Note: inverted blink servo? if so why?

x_direction = 0
y_direction = 0
blinkinterval = 0

def setup():
    # Setup code for Raspberry Pi
    myServo1.value = None
    myServo2.value = None
    myServo3.value = None
    myServo4.value = None
    global blinkinterval
    global x_direction
    global y_direction

def loop():
    #Note: Im not sure you understand that a loop func is going to loop forever, so dont put code thatll run once and then enter a while loop


    #Note: Removed the loop here as this is already being run in a loop and i dont want to multithread >:( although we might have to if we want eyes to update at the same time as recieving input
    #Note: We wouldnt have this multithreading dilema if we used an Ard

    # Replace these values with actual sensor readings
    x_pos = 512  # Example placeholder value
    y_pos = 512  # Example placeholder value

    # Map x_pos and y_pos values to servo range (assume -1 to 1 for gpiozero Servo)
    x_direction = map_val(x_pos, 0, 1023, -1, 1)
    y_direction = map_val(y_pos, 0, 1023, -1, 1)

    #Note: why custom funcs for each direction? seems kinda useless tbh
    lr_direction()
    ud_direction()

    if (time() - blinkinterval) > 3.2:  # Converted milliseconds to seconds
        blink()
    #Note: Turns out we do have to multithread becuase you put in sleep values, there are more efficient and maluable ways of doing this....
      # Add some delay for stability

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

# if __name__ == '__main__':
#     setup()
#     loop()

#Note: standalone, this code is fine and works perfectly, when we merge it with the rest of the system it wont work, can you please fix this or i will be left cleaning up your mess