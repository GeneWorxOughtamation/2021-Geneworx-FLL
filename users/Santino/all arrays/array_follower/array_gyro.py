
#Date 5/1/2022
#By Santino .J. Tomasi
#Version 1

#All imports.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase




left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
gyro_sensor = GyroSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)

gyro_sensor.reset_angle(0)

#This program uses the gyro to turn and move forward and backward.

def array_gyro(speed,distance,angle,correction_speed):


    
    while robot.distance() < distance*25.4:

        

        correction = angle+gyro_sensor.angle()


        left_motor.run(speed-correction)
        right_motor.run(speed+correction)
    

    while robot.distance() > distance*25.4:

        while gyro_sensor() != angle:

            if gyro_sensor.angle() < angle:
                left_motor.run(correction_speed)
                right_motor.run(-correction_speed)
            else:
                left_motor.run(-correction_speed)
                right_motor.run(correction_speed)
        
        left_motor.run(speed)
        right_motor.run(speed)








    