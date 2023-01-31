#!/usr/bin/env pybricks-micropython
def I2mm( inches ):
    mm = 25.4 * inches
    return mm

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""
from lib.move_elevator import eUPmovement
from lib.angle_turn import angle_turn
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase





# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
Lmotor_updown = Motor(Port.A,positive_direction=Direction.COUNTERCLOCKWISE)
Medmotor_leftright = Motor(Port.D,positive_direction=Direction.COUNTERCLOCKWISE)
gyro = GyroSensor(Port.S4,Direction.CLOCKWISE)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
# UD = up,down
# LR = left,right

def gyrom(dis, ang, speed):
    gyro.reset_angle(0)
    kp = 3
    #every time the "gost" function is used all the three variables will be swapped out with
    #  what's in the paranthesis in the order shown above.
    if I2mm(dis) >=0 : 
        while robot.distance() <= I2mm(dis):
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
        while robot.distance() >= I2mm(dis):    
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

def lever():
    eUPmovement(200, -360, 0)
    eUPmovement(200, 12, 0)


            

eUPmovement(250, -2, 850)
gyrom(17.5, 0, 200)
lever()
lever()
#lever pt2
eUPmovement(200,-360,0)
eUPmovement(200, .4,0)
#backwards
gyrom(-6, 0, 400)
eUPmovement(250, -2, -1000)
gyrom(3.5, 0, 150)
eUPmovement(200,-100,0)
eUPmovement(200,100,0)
gyrom(-20, 0, 150 )
eUPmovement(150, 0, 5)









                                                                                                                                                                                                                                                                                    


