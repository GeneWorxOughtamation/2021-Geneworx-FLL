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


def warpspeed(snumber):
    speed= [10,20,30,40,50,60,70]
    inches=[1,2,3,4,5,6,7]
    i=0
    x=len(speed)
    
    while i<x:
        i=i+1

        if speed[i-1]==snumber:
            
            while True:
                left_motor.run(speed[i-1])
                right_motor.run(speed[i-1])



def move():
    warpspeed(30)



def main():
    move()

if __name__ == "__main__":
     main()
