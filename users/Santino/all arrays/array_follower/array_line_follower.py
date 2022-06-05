
#Version 1
#Date 4/14/2022
#Maker Santino Tomasi

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

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
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)


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
        print("Line follower")
        print(robot.distance()/25.4)
        #Increases the value of i every time the program goes through the function.
        i=i+1

        #Makes sure the robot goes for the correct amount of inches.
        while robot.distance()<25.4*inches[i-1]:
            print("Line follower")
            print(robot.distance()/25.4)
            deviation = light_sensor.reflection() - threshold
            bmotor=array_speed[i-1]+deviation
            cmotor=array_speed[i-1]-deviation
            left_motor.run(bmotor)
            right_motor.run(cmotor)