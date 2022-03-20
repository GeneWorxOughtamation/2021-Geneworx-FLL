#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor 
from pybricks.parameters import Port, Direction, Color, ImageFile, SoundFile, Button
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
left_gear = Motor(Port.A)             # Define left gear -- Check This
right_gear = Motor(Port.D) 
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=114)
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S3)
gyro = GyroSensor(Port.S4,Direction.CLOCKWISE)
left_motor.reset_angle(0)
right_motor.reset_angle(0)
gyro.reset_angle(0)
 
# Initialize the drive base.
#robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
LeftLightSensor = 1
RightLightSensor = 2
GyroSensor = 3
Leftside=1
Rightside=-1
def pos_neg (number):
    if number<0:
        return(-1)
    else:
        return(1)


def move_straight_array (sensorChoice, lineSide, gain):
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
        # lineSide =  1beans
        # sensorChoice = 2
        # base_speed = 100
        # deg per sec 
        # distance = 12
        # inches
        #    cmotor=speed[i]-deviation*lineSide*gain
        # gain  = 1
    #speed=   [200, 500,  200,   500, 300, 300, 200, 300, 35]
    a=200
    speed=   [a,a,a,a,a,a,a,a,a,a,a,a,a]
    interval=[ 3,   6,   18,    35,  40,  44,  58, 60]
    angle  = [-90,   90,  0,   0,    -90,  90, 0,  0]
    LeftLightSensor = 1
    RightLightSensor = 2
    GyroSensor = 3
    Leftside=1
    Rightside=-1
    BLACK = 9
    WHITE = 85
    threshold = 50
    i=0
    x=len(speed)
    while (i<x):
        speed1=200
        speed2=25
        gyro.reset_angle(1)
        sign=pos_neg(angle[i])
        print(sign)
        abs_angle=sign*angle[i]
        speed_L=speed1*sign
        speed_R=speed1*sign*-1
        speed2_L=speed2*sign
        speed2_R=speed2*sign*-1
        if sign!=-1:
            while abs_angle > gyro.angle():
                left_motor.run(speed_L)
                right_motor.run(speed_R)
            left_motor.brake()
            right_motor.brake()
        else:
            while abs_angle < gyro.angle():
                    left_motor.run(speed_R)
                    right_motor.run(speed_L)
            left_motor.brake()
            right_motor.brake()
        
        while(robot.distance()<25.4*interval[i]):
            if(sensorChoice==LeftLightSensor):
                deviation = left_sensor.reflection() - threshold
                bmotor=speed[i]+deviation*lineSide*gain
            elif(sensorChoice==RightLightSensor):
                deviation = right_sensor.reflection() - threshold
                bmotor=speed[i]+deviation*lineSide*gain
                cmotor=speed[i]-deviation*lineSide*gain
            elif(sensorChoice==GyroSensor&sign==1):
                deviation = angle[i]-gyro.angle()
                bmotor=speed[i]-deviation*gain
                cmotor=speed[i]+deviation*gain
            elif(sensorChoice==GyroSensor):
                deviation = angle[i]+gyro.angle()
                bmotor=speed[i]+deviation*gain
                cmotor=speed[i]-deviation*gain
            left_motor.run(cmotor)            
            right_motor.run(bmotor)
            
        
        i=i+1


def turn( angle1 ):
    speed=200
    speed2=25
    gyro.reset_angle(1)
    abs_angle=pos_neg(angle1)*angle1
    sign=pos_neg(angle1)
    speed_L=speed*sign
    speed_R=speed*sign*-1
    speed2_L=speed2*sign
    speed2_R=speed2*sign*-1
    if sign!=1:
        while abs_angle < gyro.angle():
            left_motor.run(speed_L)
            right_motor.run(speed_R)
        left_motor.brake()
        right_motor.brake()
    else:
        while angle1 > gyro.angle():
            left_motor.run(speed_L)
            right_motor.run(speed_R)
        left_motor.brake()
        right_motor.brake()

def warp():
    speed=   [20, 50, 100, 200, 300, 100, 50, 35]
    interval=[ 1,  2,   4,   6,  10, 15, 16, 17]
    i=0
    x=len(speed)
    while (i<x):
        i=i+1
        while(robot.distance()<25.4*interval[i-1]):
            left_motor.run(speed[i-1])
            right_motor.run(speed[i-1])
    left_motor.brake()
    right_motor.brake()

def main():
    move_straight_array(3,1,1.25)
    

#Runs all included functions and code. 
if __name__ == "__main__":
     main()  

