#Lines up robot on black line.
#By Santino .J. Tomasi
#Date 5/32/2022
#Version 2

#Light sensors positions are figured out by looking at the front of the robot.
#For example if your are looking at the robot from the front the sensor to the left is the left light sensor.

#All imports used in program.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

#Defines the motors and sensors.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
light_sensor_left = ColorSensor(Port.S2)
light_sensor_right = ColorSensor(Port.S1)

#Defines robot.
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)

#The line up function.
def line_up():


    #The value of white on the board.
    White = 100

    #The value of black used in threshold.
    black = 9

    #The value of white used in threshold.
    white = 85

    #Defines threshold which is equal to 47.
    threshold = (black+white)/2

    #Defines run which is used to run the main while loop.
    run = True

    while run:

        #This if statment is used to figure out if both the robots color sensors reached the black line at the same time.
        if light_sensor_right.reflection() and light_sensor_left.reflection() == threshold:

            #This has the robot go backwards until it reaches white.
            while light_sensor_right.reflection() and light_sensor_left.reflection() != White:
                left_motor.run(-40)
                right_motor.run(-40)

            #This has the robot go forwards until it reaches the black line again.
            while light_sensor_right.reflection() and light_sensor_left.reflection() != threshold:
                left_motor.run(40)
                right_motor.run(40)
            #This sets run to false which ends the program.
            run = False

        #This if statment is used to figure out if the right color sensor reach the black line before the left sensor.
        if light_sensor_right.reflection() == threshold:

            #This has the robot turn until both of the sensors are equal to threshold
            while light_sensor_left.reflection() != threshold:
                right_motor.brake()
                left_motor.run(30)

            #This has the robot go backwards after turning because the robot has most likely went over the black line.
            while light_sensor_right.reflection() and light_sensor_left.reflection() != threshold:
                left_motor.run(-40)
                right_motor.run(-40)

            #This has the robot go backwards until it reaches white.
            while light_sensor_right.reflection() and light_sensor_left.reflection() != White:
                left_motor.run(-40)
                right_motor.run(-40)

            #This has the robot go forwards until it reaches the black line again.
            while light_sensor_right.reflection() and light_sensor_left.reflection() != threshold:
                left_motor.run(40)
                right_motor.run(40)
            #This sets run to false which ends the program.
            run = False

        #This if statment is used to figure out if the left color sensor reach the black line before the right sensor.
        if light_sensor_left.reflection() == threshold:

            #This has the robot turn until both of the sensors are equal to threshold.
            while light_sensor_right.reflection() != threshold:
                left_motor.brake()
                right_motor.run(30)

            #This has the robot go backwards after turning because the robot has most likely went over the black line.
            while light_sensor_right.reflection() and light_sensor_left.reflection() != threshold:
                left_motor.run(-40)
                right_motor.run(-40)

            #This has the robot go backwards until it reaches white.
            while light_sensor_right.reflection() and light_sensor_left.reflection() != White:
                left_motor.run(-40)
                right_motor.run(-40)

            #This has the robot go forwards until it reaches the black line again.
            while light_sensor_right.reflection() and light_sensor_left.reflection() != threshold:
                left_motor.run(40)
                right_motor.run(40)
            #This sets run to false which ends the program.
            run = False

        #This runs the motors until one or both the light sensors reach the black line.
        left_motor.run(40)
        right_motor.run(40)


 






        
       

