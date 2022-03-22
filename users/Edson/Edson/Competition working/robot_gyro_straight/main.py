#!/usr/bin/env pybricks-micropython

#Inches to milimeters function.
def i2mm(Inches):
    mm =25.4*Inches
    return mm 

#Seconds to miliseconds function.
def s2ms(Seconds):
    ms =1000*Seconds
    return ms 

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor 
from pybricks.parameters import Port, Direction, Color, ImageFile, SoundFile, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait 
from truck import truck_function
from moveSwitch import turn, move_straight
from perogyro import gyrom 
from competition_truck import truck_mission

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensors.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_gear = Motor(Port.A) 
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=114)
gyro = GyroSensor(Port.S4, Direction.CLOCKWISE)


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)


#Gyro function.
def drive_gyro(Distance,Speed,angle):

    robot.reset()
    gain = 0.5
     
    if robot.distance() <= Distance:
        #Gyro drive forwards.
        
        while  robot.distance() <= Distance:
            correction = (angle - gyro.angle())*(gain)
            robot.drive(Speed,correction)
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        ev3.speaker.beep()

    else:
        
        #Gyro drive backwards. 
        print(Distance, robot.distance())
        while robot.distance() >= Distance:
            correction = (angle - gyro.angle())*(gain)
            print(Distance, robot.distance(), correction)
            robot.drive(Speed,correction)
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        ev3.speaker.beep()
#End of gyro function.

#Defined colors.
yellow = (10, 6, 0) 

green = (2,8, 0)

black = (0, 1, 0)

white = (4, 9, 2)

red = (15, 1, 0)

blue = (0, 0, 2)


#Defined center function.
def center_function():
            cargo_plane()
           
#Defined left function.            
def left_function():
    #Does not do missions but is used for testing gyro. 
    ev3.speaker.say("Left Function")
    right_gear.run_target(90/0.5,700,wait=True)

#Defined right function.
def right_function():
    ev3.speaker.say("Right Function")
    cargo_ship()
   
#Defined up function.
def up_function():
    #Does not do any missions.
    ev3.speaker.say("Up Function")
    ev3.speaker.say("Moving forward 5 inches")
    robot.reset()
    drive_straight(i2mm(5), i2mm(7))
    ev3.speaker.say("Moving backward 5 inches")
    robot.reset()
    drive_backward(i2mm(-5), i2mm(-7))
    ev3.speaker.say("Moving forward 3 inches and turning 79 degrees")
    robot.reset()
    drive_straight(i2mm(3), i2mm(7))
    robot.turn(79)
    ev3.speaker.say("Turning 360 degrees")
    robot.turn(360)
    ev3.speaker.say("Move backward 3 inches")
    robot.reset()
    drive_backward(i2mm(-3), i2mm(-7))
    ev3.speaker.say("Turning negative 79 degrees")
    robot.turn(-79)


#Mission fucntions.

#Cargo ship Mission.
#Moves towards the crane then pushes it and then goes back to base.
def cargo_ship():
    ev3.speaker.say("Cargo ship mission")
    gyrom(i2mm(6.5),0,200)
    robot.turn(50)
    gyrom(i2mm(41),0,200)
    robot.turn(48)
    gyrom(i2mm(14.9),0,200)
    gyrom(i2mm(-17),0,200)
    robot.turn(-48)
    gyrom(i2mm(-41),0,200)

#Cargo Plane mission.
#Moves towards cargo plane, then moves the gears inorder to have the cargo come out,then goes back to base.
def cargo_plane():
    gyrom(i2mm(20),0,150)
    robot.turn(55)
    ev3.speaker.beep()
    robot.turn(-56)
    ev3.speaker.beep()
    gyrom(i2mm(5),0,150)
    ev3.speaker.beep()
    robot.turn(-55)
    gyrom(i2mm(2.2),0,150)
    right_gear.run_target(90/0.5,700,wait=True)
    right_gear.run_target(90/0.5,-10,wait=True)
    gyrom(i2mm(-3),0,150)
    gyrom(i2mm(-15),0,150)
#Debug program.
def wind_mill():
    gyrom(i2mm(26),0,200)
    gyrom(i2mm(-25),0,250)
    wait(s2ms(2))
    gyrom(i2mm(26),0,200)
    gyrom(i2mm(-25),0,250)
    
#Debuging function. 
def say_debug():
    ev3.speaker.say("Debug Function")
    ev3.screen.print(ev3.buttons.pressed())
    print(ev3.buttons.pressed())
    ev3.speaker.beep()
#Code which toggles the dubug function on/off.
def toggle_debug():
    wait(s2ms(2))
    while not Button.DOWN in ev3.buttons.pressed():
        say_debug()
    while Button.DOWN in ev3.buttons.pressed():
        end_debug()
#Exits the dubug function or any other program.        
def end_debug():
    ev3.speaker.say("End of Function")
    pass


#Defined checkButton function which runs all button functions included.
def checkButton():
    while True:   
        if Button.CENTER in ev3.buttons.pressed():
            center_function()
        elif Button.UP in ev3.buttons.pressed():
            up_function()
        elif Button.LEFT in ev3.buttons.pressed():
            left_function()
        elif Button.RIGHT in ev3.buttons.pressed():
            wind_mill()        
        elif Button.DOWN in ev3.buttons.pressed():
            truck_mission()
          


#Main function which runs the checkButton function.                
def main():
    while True:
        print(ev3.buttons.pressed())
        checkButton()

#Runs all included functions and code in main function. 
if 1 == 1:
    main() 
