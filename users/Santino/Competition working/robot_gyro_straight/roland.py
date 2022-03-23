# move_straight and turn Functions

# both  functions within this file
# move_straight moves using line or gyro
# turn turns to specific angle 

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
left_gear = Motor(Port.A)             # Define left gear -- Check This
right_gear = Motor(Port.D) 
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=114)
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S2)
gyro = GyroSensor(Port.S4,Direction.CLOCKWISE)
center_sensor = ColorSensor(Port.S3)
left_motor.reset_angle(0)
right_motor.reset_angle(0)
gyro.reset_angle(0)

def move_straight (base_speed, distance, lineSide, sensorChoice, gain):
    print( "running move_straight" )
    #moves using gyro or lightsensor on either side of the line using both sensors
    #  Sensor       Sensor  
    #  Side         Choice         Action
    #
    #  Leftside  LeftLightSensor   Left side of line, Left Sensor
    #  Lestside  RightLightSensor  Left Side, Right Sensor
    #  Rightside LeftLightSensor   Right Side, Left Sensor
    #  Rightside RightLightSensor  Right Side, Right Sensor
    #  N/A       GyroSensor        Uses Gyroscope, forwards or backwards
    # lineSide =  1
    # sensorChoice = 2
    # base_speed = 100 
    # distance = 12
    # gain  = 1
    LeftLightSensor = 1
    RightLightSensor = 2
    GyroSensor = 3
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
            bmotor=base_speed+deviation
            cmotor=base_speed-deviation
        print(robot.distance())
        left_motor.run(bmotor)            
        right_motor.run(cmotor)
    left_motor.brake()
    right_motor.brake()

def turn( angle,speed ):
    speed2=25
    gyro.reset_angle(1)
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
        wait(1000)
        while angle < gyro.angle():
            left_motor.run(speed2_L)
            right_motor.run(speed2_R)
        left_motor.brake()
        right_motor.brake()

#converts milimeters to inches
def i2mm(inches):
    mm = 24.5 * inches
    return mm

#turns to a specific angle
def turn( angle ):
    speed=200
    speed2=25
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
        wait(1000)
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
        wait(1000)
        while angle > gyro.angle():
            left_motor.run(-speed2_R)
            right_motor.run(-speed2_L)
        left_motor.brake()
        right_motor.brake()

def i2mm(inches):
    mm = 24.5 * inches
    return mm


def turn( angle ):
    speed=100
    speed2=25
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
        wait(1000)
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
        wait(1000)
        while angle > gyro.angle():
            left_motor.run(-speed2_R)
            right_motor.run(-speed2_L)
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
    



