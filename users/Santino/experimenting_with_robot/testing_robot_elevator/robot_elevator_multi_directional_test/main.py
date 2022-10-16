#!/usr/bin/env pybricks-micropython

#A program that move the panel on the elevator left, right, up, and down.
#By Santino .J. Tomasi
#Version 1: Oct 15,2022

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

#Needed imports
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
#Motor for up and down movement.
u2d_motor = Motor(Port.A)
#Motor for left and right movement.
l2r_motor = Motor(Port.D)

#--Not using this for now-------------------------------------------------------
# Initialize the drive base.
#robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
#--So far does not have a purpose-----------------------------------------------

#Sets run to true.
run = True

#Sets base speed to 200.
base_speed = 200

#Checks for button presses and does what is needed for each button.
while run:

    #Up and down default speed that increases or decreases.
    u2d_s = 0
    #Left and right default speed that increases or decreases.
    l2r_s = 0

    #----Checks for button presses and moves elevator accordingly---
    if Button.UP in ev3.buttons.pressed():
        u2d_s=base_speed

    if Button.DOWN in ev3.buttons.pressed():
        u2d_s=-base_speed



    #--Checks buttons that increases and decrease the base speed----
    if Button.CENTER in ev3.buttons.pressed():
        base_speed+=1

    if  Button.RIGHT in ev3.buttons.pressed() and Button.LEFT in ev3.buttons.pressed():
        base_speed-=1
    #---------------------------------------------------------------



    #----Checks for button presses and moves elevator accordingly---
    #Continued
    elif Button.RIGHT in ev3.buttons.pressed():
        l2r_s=base_speed

    elif Button.LEFT in ev3.buttons.pressed():
        l2r_s=-base_speed
    #---------------------------------------------------------------

    

    if base_speed <= 0: #Checks to see if base speed is less than or equal too zero.
        base_speed=1 #If it is less than or equal too zero than it sets base speed to equal 1.


    u2d_motor.run(u2d_s) #Runs the up and down motor.
    l2r_motor.run(l2r_s) #Runs left and right motor.

    print(base_speed) #Prints the value in base speed. 
