#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""
#Last tested fast possible speed was 143.

#Maker Santino .J. Tomasi

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait 
from pybricks.robotics import DriveBase
import threading

#Imports Speed and distance arrays in board_line file.
import board_line

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensor.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
light_sensor = ColorSensor(Port.S2) 
gyro_sensor = GyroSensor(Port.S4)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=105)

# The warpspeed function takes the distance given to it
# and runs through the array until it gets to the number that it was given
# and runs the speed associated with that distance. 

def line_follower(speed,distance):
    #Black reflection value.
    black = 9
    #White reflection value.
    white = 85
    #Threshold value which equals 47.
    threshold = (black+white) /2
    #Arrays for both speed and distance in inches.
    array_speed = speed
    inches =   distance   
    #i is a value that increases every time the program goes through the function.
    i=0
    #The length of the speed array 
    x=len(array_speed)

    #The while i<x makes the function not go over the values in the arrays.
    while i<x:
        #Increases the value of i every time the program goes through the function.
        i=i+1

        #Makes sure the robot goes for the correct amount of inches.
        while robot.distance()<25.4*inches[i-1]:
            print(light_sensor.reflection())
            deviation = light_sensor.reflection() - threshold
            bmotor=array_speed[i-1]+deviation
            cmotor=array_speed[i-1]-deviation
            left_motor.run(bmotor)
            right_motor.run(cmotor)





#Function that uses the indavidual motors to turn the robot to an angle at a specific turn speed.

def angle_turn(angle,speed):
    #Makes the robot wait 100 miliseconds which is used so the robot does not set its gyro rest angle while it is turning.
    #wait(100)
    #Sets the gyro angle to 0.
    gyro_sensor.reset_angle(0)
    #Makes the program run until it reaches the angle the user wants.
    while not gyro_sensor.angle()==angle:
        #Prints the current gyro angle.
        print(gyro_sensor.angle())
        #Tells the robot to turn either left or right.
        #For example if you want to turn the robot 90 degrees it will turn left because the gyro reads left as positive
        #so if you want to turn right it will need to go -90 degrees but you need the progam to be able to accept both negative and
        #positive numbers so it can turn both left and right that is what this part of the program does. It will turn right if the degrees is 
        #negative and left if it is positive.  
        if angle>0:
            left_motor.run(speed)
            right_motor.run(-speed)
        if angle<0:
            left_motor.run(-speed)
            right_motor.run(speed)
    

def move():
    line_follower(board_line.bl_speed,board_line.bl_distance)
    
def debug_print():
    while True:
        print(gyro_sensor.angle())


def main():
    angle_turn(-50,100)
    print(gyro_sensor.angle())
    print(gyro_sensor.angle())
    print(gyro_sensor.angle())
    
    

#Runs the main function and any functions in the main function.
if __name__ == "__main__":
     main()
