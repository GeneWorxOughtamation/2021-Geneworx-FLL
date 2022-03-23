#!/usr/bin/env pybricks-micropython
def I2mm( inches ):
    mm = 25.4 * inches
    return mm

def beep():
    ev3.speaker.beep()

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# from move_switch import turn, move_straight
#positive_Distance=Direction.COUNTERCLOCKWISE


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


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


# robot will move out of base, turn 30 degrees to the left, then turn 30 degrees to the right to go straight
#and then lift up the attatchment to leave behind the truck and to push down the bridge.

               #  Robot will push down the final bridge and return to base (x points)






