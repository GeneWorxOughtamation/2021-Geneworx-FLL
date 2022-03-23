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
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, 
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from moveSwitch import move_straight, turn

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
left_medium = Motor(Port.A)
right_medium = Motor(Port.D)
robot = DriveBase( left_motor, right_motor, 61.918, 114 )
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S2)
GyroSensor(Port.S4, Direction.CLOCKWISE)
gyro = GyroSensor(Port.S4)
LeftLightSensor = 1
RightLightSensor = 2
GyroSensor = 3
Leftside=1
Rightside=-1

#moves using line or gyro
def move_straight (base_speed, distance, sensorChoice, lineSide, gain):
    print( "running move_straight" )
    #moves using gyro or lightsensor on either side of the line using both sensors
        #  Sensor       Sensor  
        #  Side         Choice         Action
        #
        #  Leftside  LeftLightSensor   Left side of line, Left Sensor
        #  Leftside  RightLightSensor  Left Side, Right Sensor
        #  Rightside LeftLightSensor   Right Side, Left Sensor
        #  Rightside RightLightSensor  Right Side, Right Sensor
        #  N/A       GyroSensor        Uses Gyroscope, forwards or backwards
        # lineSide =  1
        # sensorChoice = 2
        # base_speed = 100
        # deg per sec 
        # distance = 12
        # inches
        # gain  = 1
    
    LeftLightSensor = 1
    RightLightSensor = 2
    GyroSensor = 3
    Leftside=1
    Rightside=-1
    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2
    gyro.reset_angle(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

    while abs(robot.distance()) <= (distance*25.4):
        if(sensorChoice==LeftLightSensor):
            deviation = left_sensor.reflection() - threshold
            bmotor=base_speed+deviation*lineSide*gain
            cmotor=base_speed-deviation*lineSide*gain
        elif(sensorChoice==RightLightSensor):
            deviation = right_sensor.reflection() - threshold
            bmotor=base_speed+deviation*lineSide*gain
            cmotor=base_speed-deviation*lineSide*gain
        elif(sensorChoice==GyroSensor):
            deviation = gyro.angle()
            bmotor=base_speed+deviation*gain
            cmotor=base_speed-deviation*gain
        left_motor.run(bmotor)            
        right_motor.run(cmotor)
    left_motor.brake()
    right_motor.brake()

#converts milimeters to inches
def i2mm(inches):
    mm = 24.5 * inches
    return mm

#turns to a specific angle
def turn( angle ):
    # turns to a specific angle or degree and waits half a second and corrects
    # angle= degree to turn to
    # withing 5 degrees
    speed=200
    speed2=30
    gyro.reset_angle(0)
    abs_angle=abs(angle)
    sign=abs(angle)/angle
    speed_L=speed*sign
    speed_R=speed*sign*-1
    speed2_L=speed2*sign
    speed2_R=speed2*sign*-1
    if sign!=-1:
        while abs_angle > gyro.angle():
            left_motor.run(speed_R)
            right_motor.run(speed_L)
        left_motor.brake()
        right_motor.brake()
        wait(500)
        while angle < gyro.angle():
            left_motor.run(speed2_L)
            right_motor.run(speed2_R)
        left_motor.brake()
        right_motor.brake()


    else:
        while angle < gyro.angle():
            left_motor.run(-speed_L)
            right_motor.run(-speed_R)
        left_motor.brake()
        right_motor.brake()
        wait(500)
        while angle > gyro.angle():
            left_motor.run(-speed2_R)
            right_motor.run(-speed2_L)
        left_motor.brake()
        right_motor.brake()

#does the unloadCargoShip mission

def unloadCargoShip():
    move_straight(200,3,3,1,1)
    move_straight(-200,3,3,1,1)
    move_straight(200,3,3,1,1)
    turn(-50)
    move_straight(300,33,3,1,1)
    turn(-40)
    move_straight(300,22,3,1,1)
    print("phase2")
    left_medium.run_time(100,1000,then=Stop.HOLD,wait=False)
   
    print("phase3")
    move_straight(-200,14,3,1,1)
    turn(-90)
    move_straight(-200,16,3,1,1)
    move_straight(200,12,3,1,1)#how close to the truck load
    turn(90)
    move_straight(-200,10,3,1,1)#how close to the line

def deliverPackage():
    move_straight(200,46,-1,3,1)
    turn(-60)
    move_straight(100,10,1,3,1)
    left_medium.run_until_stalled(1000,brake,none)


        




