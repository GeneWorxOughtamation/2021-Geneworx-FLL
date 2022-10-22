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
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
#Motor for up and down movement.
u2d_motor = Motor(Port.A)
#Motor for left and right movement.
l2r_motor = Motor(Port.D)

run = True

def move_elevator(ud_speed,lr_speed,ud_angle,lr_angle):

    i = 0
    x = len(up_speed)

    while i<x:
        
        while run:
            if ud_angle[0] == u2d_motor.angle() and lr_angle[0] == l2r_motor.angle():
                run = False
                
            u2d_motor.run_target(ud_speed[i], ud_angle[i], then=Stop.HOLD, wait=True)
            l2r_motor.run_target(lr_speed[i], lr_angle[i], then=Stop.HOLD, wait=True)

            i+=1

        

