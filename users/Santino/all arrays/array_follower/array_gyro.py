
#Date 5/1/2022
#By Santino .J. Tomasi
#Version 2

#All imports.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

#Imports all the arrays used in this program.
import array_gyro_arrays


#
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
gyro_sensor = GyroSensor(Port.S4)

#Sets robot to equal DriveBase.
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)

#Resets the gyro angle at the beginning of the program.
gyro_sensor.reset_angle(0)

#This program uses the gyro to turn and move forward and backward.

def array_gyro(distance,speed,angle):

    #Sets inches to equal the value of distance.
    inches = distance

    #i is a value that increases every time the program goes through the function.
    i=0

    #The length of the distance array.
    x=len(distance)

    #The while i<x makes the function not go over the values in the arrays.
    while i<x:

        #Increases the value of i every time the program goes through the function.
        i=i+1

        #Makes the robot run while the distance is greater than the current valuse in the distance array.
        while robot.distance() > 25.4*inches[i-1]:


            #The correction is the value that is used to be added or subtracted by the current speed.
            correction = angle[i-1]+gyro_sensor.angle()

            #This keeps the robot going straight for a angle.
            left_motor.run(speed[i-1]+correction)
            right_motor.run(speed[i-1]-correction)

        #Makes the robot run while the distance is less than than the current valuse in the distance array.
        while robot.distance() < 25.4*inches[i-1]:


            #The correction is the value that is used to be added or subtracted by the current speed.
            #If you would like the robot to turn left for a positive angle then subtract the angle by the gyro sensor angle.
            #If you would like the robot to turn left for a negative angle then add the angle by the gyro sensor angle. 
            correction = angle[i-1]-gyro_sensor.angle()

            #This keeps the robot going straight for a angle.
            left_motor.run(speed[i-1]+correction)
            right_motor.run(speed[i-1]-correction)
        

        

            

            

            

                    

        


            

        
       
        










    