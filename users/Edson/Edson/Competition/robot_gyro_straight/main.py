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
from roland import turn
from roland import unloadCargoShip  

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensors.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE )
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE )
right_gear = Motor(Port.A)
gyro = GyroSensor(Port.S4)
light = ColorSensor(Port.S3)



# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=115)


#Gyro function.
def drive_gyro(Distance,Speed,angle):
    gain = -3
     
    if robot.distance() <= Distance:
        #Gyro drive forwards.

        while  robot.distance() <= Distance:
            correction = (angle - gyro.angle())*(gain)
            robot.drive(Speed,correction)
        robot.reset()
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
            robot.reset()
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
            ev3.speaker.say("Center Function")
            cargo_plane()
           
#Defined left function.            
def left_function():
    #Does not do missions but is used for testing gyro. 
    ev3.speaker.say("Left Function")
    drive_gyro(i2mm(30),200,0)

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
    drive_gyro(i2mm(6.5),70,0)
    robot.turn(50)
    drive_gyro(i2mm(41),70,0)
    robot.turn(48)
    drive_gyro(i2mm(14.9),70,0)
    drive_gyro(i2mm(-17),-70,0)
    robot.turn(-48)
    drive_gyro(i2mm(-41),-70,0)

#Cargo Plane mission.
#Moves towards cargo plane, then moves the gears inorder to have the cargo come out,then goes back to base.
def cargo_plane():
    ev3.speaker.say("Cargo plane mission")
    ev3.screen.load_image(ImageFile.RIGHT)
    ev3.screen.print(light.rgb())
    drive_gyro(i2mm(14.5),i2mm(7),0)
    robot.turn(-45)
    robot.turn(45)
    drive_gyro(i2mm(12.9),i2mm(7),0)
    robot.turn(45)
    right_gear.run_target(90/0.5,310,wait=True)
    right_gear.run_target(90/0.5,-170,wait=True)
    drive_gyro(i2mm(-27),-90,0)

#Debug program.

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
print(light.rgb())
def checkButton():
    while True:   
        if Button.CENTER in ev3.buttons.pressed():
            center_function()
        elif Button.UP in ev3.buttons.pressed():
                up_function()
        elif Button.LEFT in ev3.buttons.pressed():
                left_function()
        elif Button.RIGHT in ev3.buttons.pressed():
                right_function()

        elif Button.DOWN in ev3.buttons.pressed():
            toggle_debug()
          


#Main function which runs the checkButton function.                
def main():
    while True:
        print(ev3.buttons.pressed())
        checkButton()

#Runs all included functions and code in main function. 
if __name__ == "__main__":
     main() 
