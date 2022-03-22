#!/usr/bin/env pybricks-micropython

def I2mm( inches ):
    mm = 25.4 * inches
    return mm

def mm2I(millameters):
    I = millameters / 25.4
    return I

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math


# Initialize the drive base.
    

def beep():
    ev3.speaker.beep()



# Create your objects here.
ev3 = EV3Brick()
  

# Write your program here.
ev3.speaker.beep()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_gear = Motor(Port.D, Direction.CLOCKWISE)
left_gear = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=114)
gyro = GyroSensor(Port.S4,Direction.CLOCKWISE)
rlight = ColorSensor(Port.S2)



gear_speed = 100
gear_rotation_angle = 150

#run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)



# gyrom function go stright and back a distance "dis" following and angle "ang"
def gyrom(dis, ang, speed):
    gyro.reset_angle(0)
    kp = 3
    #every time the "gost" function is used all the three variables will be swapped out with
    #  what's in the paranthesis in the order shown above.
    if dis >=0 : 
        while robot.distance() <= dis:
            print( robot.distance() )     
            correction = (ang - gyro.angle())*kp
            robot.drive(speed,correction)
            #Robot will stop and the large motor's distance will be reset.
            #The angle of the gyro sensor will also be reset back to zero.
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        print( robot.distance() )
        left_motor.reset_angle(0)
        right_motor.reset_angle(0)
    
    else :
        while robot.distance() >= dis:    
            correction = (ang - gyro.angle())*kp
            robot.drive(-speed,correction)
            #Robot will stop and the large motor's distance will be reset.
            #The angle of the gyro sensor will also be reset back to zero.
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        print( robot.distance() )
        left_motor.reset_angle(0)
        right_motor.reset_angle(0)
#tells the robot to turn the Right medium motor a certain degree at a certain speed. Also resets the angle of
#the medium motor.
def Rgear(S, RA):
    right_gear.reset_angle(0)
    right_gear.run_angle(S, RA)

uniarray = [[0,50,100,150,200], [250,300,350,400,450], [500,550,600,650,700], [750,800,850,900,950,1000]]

def ArrayM(maxd):
    A = 25
    B = 100
    C = 300
    D = 300
    E = 150
    F = 50
    G = 150
    H = 200
    I = 175
    A1 = [A, B, C, D, E, F, G, H, I]
    s=len(A1)
    interval=maxd/(len(A1)+1)
    i=0
    while(i<=s):
        i=i+1
        print (I2mm(maxd))
        while robot.distance() < 25.4*interval*i:
            right_motor.run( A1[i-1] )
            left_motor.run( A1[i+1] )


speed = [200,75,100,150,175,200,150,125,100,75,50,100,150,175,200,150,100,50,0]
def fl(d, kp):
    i = 0
    while robot.distance() <= I2mm(d):
        i = i+1
        correction = ((45 - rlight.reflection())*kp)
        right_motor.run(speed [i]+correction)
        left_motor.run(speed [i]-correction)


fl(60, 1)

``





#ArrayM(30)
    