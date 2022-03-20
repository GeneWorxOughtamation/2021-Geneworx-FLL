#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port,Direction
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
 
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=114)

speed = [100,200,300,400,500,400,300,200,100]
interval=3
i=0
while(i<6):
    i=i+1
    while(robot.distance()<=25.4*interval*i):
        left_motor.run(speed[i-1])
        right_motor.run(speed[i-1])
left_motor.brake()
right_motor.brake()

