#!/usr/bin/env pybricks-micropython

#By Santino Tomasi
#Date Nov 27,2022

#All imports.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

#Imports library.
from lib.angle_turn import angle_turn
from lib.array_gyro import array_gyro
from lib.move_elevator import eUPmovement
from lib.gyrom import gyrom

def I2mm( inches ):
    mm=25.4*inches
    return mm

#Sets motors and gyro.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
gyro_sensor = GyroSensor(Port.S4)
#Sets robot to equal DriveBase.
robot = DriveBase(left_motor, right_motor, wheel_diameter=62.4, axle_track=115)


#T.v. show. 

gyrom(16,0,690)

gyrom(-2,0,100)
robot.turn(70)
gyrom(17,0,200)

robot.turn(-125)

gyrom(7,0,150)

gyrom(-4,0,100)

gyrom(7,0,150)
gyrom(-4,0,100)
gyrom(7,0,150)

gyrom(-4,0,100)
gyrom(5,0,150)
gyrom(-5,0,100)

robot.turn(-140)
robot.straight(I2mm(50))
