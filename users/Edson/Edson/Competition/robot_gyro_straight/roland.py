#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

#import files
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#sensor setup
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
robot = DriveBase( left_motor, right_motor, 61.918, 114 )
        #robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axel_track=114)
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S2)
GyroSensor(Port.S4, Direction.CLOCKWISE)
gyro = GyroSensor(Port.S4)

#explain move_switch
    #  Sensor       Sensor  
    #  Side         Choice         Action
    #
    #    1            1          Left side of line, Left Sensor
    #    1            2          Left Side, Right Sensor
    #   -1            1          Right Side, Left Sensor
    #   -1            2          Right Side, Right Sensor
    #   -1            3          Uses Gyroscope, moves in current direction

# defalt varibles
sensorSide =  1
sensorChoice = 2
base_speed = -100 
distance = 12*25.4
PROPORTIONAL_GAIN  = 1
BLACK = 9
WHITE = 85
    #while 1:   # placeholder to keep indent proper

def move_switch ( sensorSide, sensorChoice, base_speed, distance, BLACK, WHITE, PROPORTIONAL_GAIN ):
    
    print( "running move_switch" )
    # Calculate the light threshold. Choose values based on your measurements.
    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2

    # Set the drive speed at 100 millimeters per second.
    DRIVE_SPEED = -50

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    #PROPORTIONAL_GAIN = 1.5
    #base_speed =-150
    #sensorSide=-1
    #sensorChoice=1
    gyro.reset_angle(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    # Start following the line until defined distance.
    while robot.distance() >= (distance*25.4):
        
        if(sensorChoice==1):
            # Calculate the deviation from the threshold.
            deviation = left_sensor.reflection() - threshold
        elif(sensorChoice==2):
            deviation = right_sensor.reflection() - threshold

        else:
            # Calculate the deviation from the threshold.
            deviation = gyro.angle()
    

        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation
        #percent = deviation  50

        # Set the drive base speed and turn rate.
        #robot.drive(DRIVE_SPEED, turn_rate)
        bmotor=base_speed+deviation*sensorSide
        cmotor=base_speed-deviation*sensorSide

        left_motor.run(bmotor)
        right_motor.run(cmotor)
        # You can wait for a short time or do other things in this loop.
        #wait(1)
    left_motor.brake()
    right_motor.brake()

def i2mm(inches):
    mm = 24.5 * inches
    return mm


def turn (angle, speed):
    gyro.reset_angle(1)
    abs_angle=abs(angle)
    sign=abs(angle)/angle
    speed_L=speed*sign
    speed_R=speed*sign*-1
    if sign!=-1:
        while abs_angle > gyro.angle():
            left_motor.run(speed_R)
            right_motor.run(speed_L)
            print("positive")
        left_motor.brake()
        right_motor.brake()
    else:
        while angle < gyro.angle():
            left_motor.run(speed_L)
            right_motor.run(speed_R)
            print("negitive")
        left_motor.brake()
        right_motor.brake()



def unloadCargoShip():
    move_switch(-1, 3, -200, 3, 9, 85, 1)
    turn(-45, 50)
    move_switch(-1, 3, -300, 43, 9, 85, 1)
    turn(-45, 50)
    print("phase2")
    move_switch(-1, 3, -100, 13, 9, 85, 1)
    print("phase3")
    move_switch(-1, 3, 200, 6, 9, 85, 1)
    



