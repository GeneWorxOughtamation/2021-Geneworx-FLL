#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#Inches to milimeters function.
def i2mm(Inches):
    mm =25.4*Inches
    return mm 

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensors.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE )
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE )
right_gear = Motor(Port.A)
gyro = GyroSensor(Port.S4)
gain=.25
#Forwards gyro function.
def drive_straight(Distance, Speed):

    #Gyro Sensor code. 

    gyro.reset_angle(0)

    while robot.distance() <= Distance:
        correction = (0 - gyro.angle())*(gain)
        print(Distance, robot.distance(), correction)
        robot.drive(Speed,correction)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    ev3.speaker.beep()

#Backwards gyro function.
def drive_backward(Distance, speed):

    #Gyro Sensor code. 

    gyro.reset_angle(0)

    while robot.distance() >= Distance:
        correction = (0 - gyro.angle())*(gain)

        robot.drive(speed,correction)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    ev3.speaker.beep()

#End of gyro functions forwards, backwards.
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)

#def Engine(): 
    #drive_gyro(i2mm(25), 100)
    #robot.turn(-25)
    #robot.turn(75)
    #drive_gyro(i2mm(16), 100)
