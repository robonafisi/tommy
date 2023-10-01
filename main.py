import cv2
import numpy as np
from Arm_Lib import Arm_Device
import time

# Initialize the Arm
arm = Arm_Device()

arm.Arm_serial_servo_write(1, 10, 500)
time.sleep(3)

arm.Arm_serial_servo_write(1, 55, 500)
time.sleep(3)

arm.Arm_serial_servo_write(1, 135, 500)
time.sleep(3)

arm.Arm_serial_servo_write(1, 185, 500)
