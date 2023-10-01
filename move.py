from Arm_Lib import Arm_Device
import threading
import time



def move_arm(pos):
    arm.Arm_serial_servo_write(1, pos, 500)
    time.sleep(.5)

def schedule_moves():
    time.sleep(3)  # Wait for 30 seconds
    move_arm(90)

    time.sleep(3)  # Wait for another 30 seconds (total 60 seconds from start)
    move_arm(0)

    time.sleep(3)
    move_arm(180)

    time.sleep(3)
    move_arm(0)

    time.sleep(3)  # Wait for another 30 seconds (total 90 seconds from start)
    move_arm(270)

    time.sleep(3)
    move_arm(0)

# Initialize the Arm
def call_arm():
    arm = Arm_Device()

    arm.Arm_serial_servo_write(1,0,500)
    time.sleep(.5)

    # Start the scheduled arm movements in a separate thread
    t = threading.Thread(target=schedule_moves)
    t.start()

    # The main thread remains free here
    print("Main thread is free!")