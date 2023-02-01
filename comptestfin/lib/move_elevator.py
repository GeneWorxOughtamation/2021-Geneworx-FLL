#By Peiro Gammara

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

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


def eUPmovement(speed, UP ,LEFT):
    if UP >= 0:
        while Lmotor_updown.angle() <= UP:
            Lmotor_updown.run_target(speed, UP)
            if Lmotor_updown.angle() >= UP:
                break

    elif UP <= 0:
        while Lmotor_updown.angle() >= UP:
            Lmotor_updown.run_target(speed, UP)
            if Lmotor_updown.angle() <= UP:
                break

    if LEFT >= 0:
        while Medmotor_leftright.angle() <= LEFT:
            Medmotor_leftright.run_target(speed, LEFT)
            if Medmotor_leftright.angle() >= LEFT:
                break


    elif LEFT <= 0:
        while Medmotor_leftright.angle() >= LEFT:
            Medmotor_leftright.run_target(speed, LEFT)
            if Medmotor_leftright.angle() <= LEFT:
                break