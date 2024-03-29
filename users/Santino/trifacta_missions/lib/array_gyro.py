
#Date 5/1/2022
#By Santino .J. Tomasi
#Version 2

#Max speed
#So far it does not matter and all speeds are equaliy inaccuret

#List of fastest times.
#14 seconds Date 5/31.2022 Time 7:00 pm
#17 seconds Date 5/31/2022 Time 6:38 pm
#18 seconds Date 5/24/2022 Time 8:25 pm
#21 seconds Date 5/24/2022 Time 8:22 pm
#22 seconds Date 5/24/2022 Time 8:18 pm
#29 seconds Date 5/24/2022 Time 8:07 pm
#34 seconds Date 5/24/2022 Time not sure


#All imports.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor,GyroSensor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase


#Sets motors and gyro.
left_motor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
gyro_sensor = GyroSensor(Port.S4)

#Sets robot to equal DriveBase.
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)


#This program uses the gyro to turn and move forward and backward.

def array_gyro(distance,speed,angle,roll):

    #Resets the gyro angle at the beginning of the program.
    gyro_sensor.reset_angle(0)


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

        if inches[i-1] >= 0:

            if robot.distance() < 25.4*inches[i-1]:
                #Makes the robot run while the distance is less than than the current valuse in the distance array.
                while robot.distance() < 25.4*inches[i-1]:

                    print("Gyro program move forward")
                    print("Also robot speed :"+str(speed[i-1])+":")
                    print("And robot distance :"+str(distance[i-1])+":")
                    print("i = "+str(i))
                    print(robot.distance()/25.4)


                    #The correction is the value that is used to be added or subtracted by the current speed.
                    #If you would like the robot to turn left for a positive angle then subtract the angle by the gyro sensor angle.
                    #If you would like the robot to turn left for a negative angle then add the angle by the gyro sensor angle. 
                    correction = angle[i-1]-gyro_sensor.angle()*1.2

                    #This keeps the robot going straight for a angle.
                    left_motor.run(speed[i-1]+correction)
                    right_motor.run(speed[i-1]-correction)

            elif robot.distance() > 25.4*inches[i-1]:
                #Makes the robot run while the distance is less than than the current valuse in the distance array.
                while robot.distance() > 25.4*inches[i-1]:

                    print("Gyro program move backward")
                    print("Also robot speed :"+str(speed[i-1])+":")
                    print("And robot distance :"+str(distance[i-1])+":")
                    print("i = "+str(i))
                    print(robot.distance()/25.4)


                    #The correction is the value that is used to be added or subtracted by the current speed.
                    #If you would like the robot to turn left for a positive angle then subtract the angle by the gyro sensor angle.
                    #If you would like the robot to turn left for a negative angle then add the angle by the gyro sensor angle. 
                    correction = angle[i-1]-gyro_sensor.angle()*1.2

                    #This keeps the robot going straight for a angle.
                    left_motor.run(speed[i-1]-correction)
                    right_motor.run(speed[i-1]+correction)

        if roll[i-1] == 1:
            left_motor.brake()
            right_motor.brake()


        #Runs the turn program if the current amount of inches is equal to zero.
        if inches[i-1] == 0:
        
            #Tells the robot to run the next part of the program only if the gyro angle is not equal to the current angle. 
            while gyro_sensor.angle() != angle[i-1]:

                #This if statement is used to figure out if the the wanted angle is positive.
                if angle[i-1] > 0:
                    left_motor.run(speed[i-1])
                    right_motor.run(-speed[i-1])

                #This if statement is used to figure out if the the wanted angle is negative.
                if angle[i-1] < 0:
                    left_motor.run(-speed[i-1])
                    right_motor.run(speed[i-1])

                #This if statement is used to figure out if the wanted angle is less than the current angle.
                if angle[i-1] < angle[i-2]:
                    left_motor.run(-speed[i-1])
                    right_motor.run(speed[i-1])

                #This if statement is used to figure out if the wanted angle is greater than the current angle.
                if angle[i-1] > angle[i-2]:
                    left_motor.run(speed[i-1])
                    right_motor.run(-speed[i-1])

                #Tells the robot to stop once it reaches the correct angle.
                if gyro_sensor.angle() == angle[i-1]:
                    #The robot waits so that it does not stop while it is turn back to the correct angle if it goes over.
                    wait(11)
                    left_motor.brake()
                    right_motor.brake()

        
    gyro_sensor.reset_angle(0)