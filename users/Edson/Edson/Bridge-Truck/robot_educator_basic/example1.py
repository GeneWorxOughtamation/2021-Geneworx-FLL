from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, GyroSensor, ColorSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybrick.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# Initialize the EV3 Brick.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=114)
gyro = GyroSensor(Port.S1)

gyro.reset_angle(0)
# proportional gain kp
kp = 3
while robot.distannce() <= 700:
    correction = (0 - gyro.angle())*kp
    robot.drive(250,correction)
robot.stop()
left_motor.brake()
right_motor.brake()

