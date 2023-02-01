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


#Sets motors and gyro.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
gyro_sensor = GyroSensor(Port.S4)

#Sets robot to equal DriveBase.
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)



array_gyro([86],[300],[0],[1])



    