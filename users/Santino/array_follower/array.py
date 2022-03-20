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
import threading

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=105)


def warpspeed():
    speed= [  100, 150, 200, 200, 200, 200, 150, 100, 80,  70, 60,60,70,80,100,150,200,200,200,200]
    inches=[   1,   2,   3,   4,   5,   6,   7,   8,   9,  10, 11,12,13,14, 15, 16, 17, 18, 19, 20]
    #inches for turn speed.
    #Inches     10, 11, 12, 13
    turnspeed=[-50,-40,-40,-50]
    i=0
    x=len(speed)
    turn=[10,11,12,13]
    while i<x:
        i=i+1
        while i==turn:
            right_motor.run(speed[i-1])
            left_motor.run(turnspeed[i-1])

        while robot.distance()<25.4*inches[i-1]:
            left_motor.run(speed[i-1])
            right_motor.run(speed[i-1])

def main():
    warpspeed()


if __name__ == "__main__":
     main()
