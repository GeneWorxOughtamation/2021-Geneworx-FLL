#!/usr/bin/env pybricks-micropython

def i2mm(Inches):
    mm =25.4*Inches
    return mm 

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=105)
light = ColorSensor(Port.S2)
reflection = 30
pg = 1.2
speed = 100
distance = i2mm(20)
reflection = 30
pg = 1.2
speed = 200

#program
#pg = portaional gain 

def line_following(length):
    while robot.distance() <= length*25.4:
        correction = (reflection - light.reflection())*pg
        
        right_motor.run(speed)
        left_motor.run(speed)
    robot.stop()
    left_motor.brake()
    right_motor.brake()

def main():
    line_following(20)
if __name__ == "__main__":
    main()
