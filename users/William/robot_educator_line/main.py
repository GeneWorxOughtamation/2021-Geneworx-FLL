#!/usr/bin/env pybricks-micropython
#Inches to milimeters function.
def i2mm(Inches):
    mm =25.4*Inches
    return mm 

#Seconds to miliseconds function.
def s2ms(Seconds):
    ms =1000*Seconds
    return ms 


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the motors.
ev3 = EV3Brick()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=105)
light = ColorSensor(Port.S2)
distance = i2mm(12)
reflection = 30
pg = 1.2
speed = 200

#program
#pg = portaional gain 

Motor_speed = 300

#motor_distance 
while (True):
    right_motor.run_target(Motor_speed, distance, wait=False)
    left_motor.run_target(Motor_speed, distance, wait=False)