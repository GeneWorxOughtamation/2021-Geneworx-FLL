def I2mm( inches ):
    mm=25.4*inches
    return mm

#Imports all needed builtin programs.
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
gyro = GyroSensor(Port.S4)

# Initialize the drive base.                
robot = DriveBase(left_motor, right_motor, wheel_diameter=62.4, axle_track=115)


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