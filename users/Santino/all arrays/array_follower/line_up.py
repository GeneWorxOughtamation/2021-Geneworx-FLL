#Lines up robot on black line.
#By Santino .J. Tomasi
#Date 5/32/2022
#Version 1

#Light sensors positions are figured out by looking at the front of the robot.
#For example if your are looking at the robot from the front the sensor to the left is the left light sensor.


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
light_sensor_left = ColorSensor(Port.S2)
light_sensor_right = ColorSensor(Port.S1)

robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)


def line_up():


        
    White = 100

    black = 9

    white = 85

    threshold = (black+white)/2

    run = True

    while run:

        if light_sensor_right.reflection() and light_sensor_left.reflection() == threshold:

            while light_sensor_right.reflection() and light_sensor_left.reflection() != White:
                left_motor.run(-40)
                right_motor.run(-40)

            while light_sensor_right.reflection() and light_sensor_left.reflection() != threshold:
                left_motor.run(40)
                right_motor.run(40)
            run = False

        left_motor.run(40)
        right_motor.run(40)









        
        

