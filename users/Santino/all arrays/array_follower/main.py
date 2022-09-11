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
from line_up import line_up
import threading

#Imports Speed and distance arrays in board_line file.
import board_line

#Imports arrays from angle_arrays file.
import angle_arrays

#Imports arrays from array_gyro file.
import array_gyro_arrays

#Imports function test arrays
import function_test_arrays
import test7
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
    line_follower(board_line.bl_speed,board_line.bl_distance,board_line.bl_sensor,board_line.bl_side)
    

def angle_turn_test():
    angle_turn(angle_arrays.array_angle,angle_arrays.array_speed,angle_arrays.array_correction)

def array_gyro_test():
    array_gyro(array_gyro_arrays.distance_array,array_gyro_arrays.speed_array,array_gyro_arrays.angle_array,array_gyro_arrays.roll_array)

def array_gyro_sixfeet_test():
    array_gyro(array_gyro_arrays.distance_six_feet_test,array_gyro_arrays.speed_six_feet_test,array_gyro_arrays.angle_six_feet_test,array_gyro_arrays.roll_six_feet_test)

def line_up_test():
    line_up()

def function_test():
    #                      Distance array         ,          Speed array           ,           Angle array          ,          Roll array
    array_gyro(function_test_arrays.distance_array,function_test_arrays.speed_array,function_test_arrays.angle_array,function_test_arrays.roll_array)
    #                  Line speed array          ,           Line distance 
    line_follower(function_test_arrays.line_speed,function_test_arrays.line_distance)
    #                      Distance array2         ,          Speed array2           ,           Angle array2          ,          Roll array2
    array_gyro(function_test_arrays.distance_array2,function_test_arrays.speed_array2,function_test_arrays.angle_array2,function_test_arrays.roll_array2)
    #                  Line speed array2          ,           Line distance array2
    line_follower(function_test_arrays.line_speed2,function_test_arrays.line_distance2)

def test():
    array_gyro(test7.array_distance,test7.array_speed,test7.array_angle,test7.array_roll)

def main():
   line_follower_test()
   
    



#Runs the main function and any functions in the main function.
if __name__ == "__main__":
     main()
