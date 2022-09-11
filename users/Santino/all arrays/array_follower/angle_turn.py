
#Version 1
#Date 4/14/2022
#Maker Santino Tomasi

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
gyro_sensor = GyroSensor(Port.S4)

# Initialize the drive base.                
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)


#Function that uses the indavidual motors to turn the robot to an angle at a specific turn speed.
#Inorder to use this function you must use an array for ALL values.

#------------------------------------
#Do not use negative correction speed.
#Do not use negative speed.
#------------------------------------
def angle_turn(angle,speed,correction_speed):

    #i is a value that increases every time the program goes through the function.
    i=0

    #The length of the angle array.
    x=len(angle)

    #The while i<x makes the function not go over the values in the arrays.
    while i<x:

        #Increases the value of i every time the program goes through the function.
        i=i+1
        
        #Sets the gyro angle to 0 so that when the function starts the gyro angle starts out at the correct beginning angle.
        gyro_sensor.reset_angle(0)

        #Tells the robot to run the next part of the program only if the gyro angle is not equal to the current angle. 
        while not gyro_sensor.angle()==angle[i-1]:

        #Prints the current gyro angle.
            print(gyro_sensor.angle())

        #Tells the robot to turn either left or right.
        #For example if you want to turn the robot 90 degrees it will turn left because the gyro reads left as positive
        #so if you want to turn right it will need to go -90 degrees but you need the progam to be able to accept both negative and
        #positive numbers so it can turn both left and right that is what this part of the program does. It will turn right if the degrees is 
        #negative and left if it is positive. 

        
            #Figures out if the angle is positive.
            if angle[i-1]>0:

                #Tells robot to go back if it goes to much and goes past the angle.
                while gyro_sensor.angle()>angle[i-1]:

                    #Turns the robot wheel motors in different directions from each other 
                    #so the robot turns left.
                    left_motor.run(-correction_speed[i-1])
                    right_motor.run(correction_speed[i-1])
                
                #This turns the robot past the given angle but
                #the robot corrects itself in the while loop above.
                left_motor.run(speed[i-1])
                right_motor.run(-speed[i-1])

            #Figures out if the angle is negative.
            if angle[i-1]<0:
                #Tells robot to go back if it goes to much and goes past the angle.
                while gyro_sensor.angle()<angle[i-1]:

                    #Turns the robot wheel motors in different directions from each other 
                    #so the robot turns right.
                    left_motor.run(correction_speed[i-1])
                    right_motor.run(-correction_speed[i-1])
                    
                #This turns the robot past the given angle but
                #the robot corrects itself in the while loop above.
                left_motor.run(-speed[i-1])
                right_motor.run(speed[i-1])

            #Tells the robot to stop once it reaches the correct angle.
            if gyro_sensor.angle()==angle[i-1]:
                #The robot waits so that it does not stop while it is turn back to the correct angle if it goes over.
                wait(11)

                #Stops the robot.
                left_motor.brake()
                right_motor.brake()