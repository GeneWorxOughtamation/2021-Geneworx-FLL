#!/usr/bin/env pybricks-micropython

#Maker Santino Tomasi
#Version 1
#Date 4/14/2022

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""
#Last tested fast possible speed was 143.


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait 
from pybricks.robotics import DriveBase
from angle_turn import angle_turn
from array_line_follower import line_follower
from array_gyro import array_gyro
import threading

#Imports Speed and distance arrays in board_line file.
import board_line

#Imports arrays from angle_arrays file.
import angle_arrays

#Imports arrays from array_gyro file.
import array_gyro_arrays

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensor.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
light_sensor = ColorSensor(Port.S2) 
gyro_sensor = GyroSensor(Port.S4)

# Initialize the drive base.                
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)


def line_follower_test():
    line_follower(board_line.bl_speed,board_line.bl_distance)
    

def angle_turn_test():
    angle_turn(angle_arrays.array_angle,angle_arrays.array_speed,angle_arrays.array_correction)

def array_gyro_test():
    array_gyro(array_gyro_arrays.distance_array,array_gyro_arrays.speed_array,array_gyro_arrays.angle_array,array_gyro_arrays.roll_array)

def array_gyro_sixfeet_test():
    array_gyro(array_gyro_arrays.distance_six_feet_test,array_gyro_arrays.speed_six_feet_test,array_gyro_arrays.angle_six_feet_test,array_gyro_arrays.roll_six_feet_test)

def main():
   array_gyro_test()
   
    



#Runs the main function and any functions in the main function.
if __name__ == "__main__":
     main()
