from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase


# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensor.

#Sets left_motor to be able to use the motor in port B. 
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)

#Sets left_motor to be able to use the motor in port C. 
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)

#Sets light_sensor to be able to use the color sensor in port 2.
light_sensor = ColorSensor(Port.S2)
#Sets gyro_sensor to be able to use the gyro sensor in port 4.
gyro_sensor = GyroSensor(Port.S4)

# Initialize the drive base.                
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)

def reset_wall(updown, leftright):
    if updown >= 0:
        while Lmotor_updown.angle() <= updown:
            Lmotor_updown.run_target(speed, updown)
            if Lmotor_updown.angle() >= updown:
                break

    elif updown <= 0:
        while Lmotor_updown.angle() >= updown:
            Lmotor_updown.run_target(speed, updown)
            if Lmotor_updown.angle() <= updown:
                break


     if leftright >= 0:
            while Medmotor_leftright.angle() <= leftright:
            Medmotor_leftright.run_target(speed, leftright)
            if Medmotor_leftright.angle() >= leftright:
                break


    elif leftright  <= 0:
        while Medmotor_leftright.angle() >= leftright:
            Medmotor_leftright.run_target(speed, leftright)
            if Medmotor_leftright.angle() <= leftright:
                break
