#!/usr/bin/env pybricks-micropython
#!/usr/bin/env pybricks-micropython
def I2mm( inches ):
    mm = 25.4 * inches
    return mm

def beep():
    ev3.speaker.beep()

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
#positive_Distance=Direction.COUNTERCLOCKWISE


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
#------------------
# Write your program here.
ev3.speaker.beep()
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_gear = Motor(Port.D, Direction.CLOCKWISE)
left_gear = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=61.918, axle_track=114)
gyro = GyroSensor(Port.S4,Direction.CLOCKWISE)



gear_speed = 100
gear_rotation_angle = 150




def speed(smax, dist): 
    # smax=max speed,dist=distance
    
    # x=0.2*dist =20% of dist
    # y=0.8*dist=80% of dist
    # mi=slope increase
    # md=slope decrease
    # si=initial spped
    # robot.distance is a global variable
     robot.drive=robot.distance()
     d=abs(dist) 
     si=0.2*smax
     x=0.20*d
     y=0.8*d
     mi=(smax-si)/x
     md=smax/(y-d)
     if abs(robot.drive) <x:
         s=si+mi*abs(robot.drive)
     if abs(robot.drive)>=x and abs(robot.drive)<=y:
         s=smax
     if abs(robot.drive) >=y and abs(robot.drive)<=d:
         s=md*(abs(robot.drive)-d)+si
     #print(s)
     return s
         

#run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)


# gyrom function go stright and back a distance "dist in inches" following and angle "ang" 
# with maximjun spee sm=smax
def gyrom(dist, ang, smax):
    gyro.reset_angle(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    dis=I2mm(dist)
    sm=smax
    kp = 3
    #every time the "gost" function is used all the three variables will be swapped out with
    #  what's in the paranthesis in the orobot.driveer shown above.
    if dis >=0 :
         
        while robot.distance() <= dis:
             #print( robot.distance() )     
             correction = (ang - gyro.angle())*kp
             #s=sm
             s=speed(sm,dis)
             robot.drive(s,correction)
            #Robot will stop and the large motor's distance will be reset.
            #The angle of the gyro sensor will also be reset back to zero.
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        
    else :
        
        while robot.distance() >= dis:    
             correction = (ang - gyro.angle())*kp 
             #s=sm
             s=speed(sm,dis)
             robot.drive(-s,correction)
             #Robot will stop and the large motor's distance will be reset.
             #The angle of the gyro sensor will also be reset back to zero.
        robot.stop()
        left_motor.brake()
        right_motor.brake()
        #print( robot.distance() )
        #left_motor.reset_angle(0)
        #right_motor.reset_angle(0)


SA = [50, 75, 100, 125, 150, 175]
    print (1)
SA
 
#ef speedAmax(SA, MaxD):
    # local variables
    #X = MaxD*0.20
    #y = MaxD*0.40
    #z = MaxD*0.60
    #W = MaxD*0.80
    #V = MaxD
    #D = robot.distance()
    

    #while D < X SA [0]
        #robot.drive(0, SA)
    #while D > X and < y SA [1]
        #robot.drive(0, SA)
    #while D > y and < z SA [2]
        #robot.drive(0, SA)
    #while D > z and < W SA [3]
        #robot.drive(0, SA)
    #while D > W and < V SA [4]
        #robot.drive(0, SA)
    #while D => V SA [5]
        #robot.drive(0, SA)
        #robot.stop()
        #right_motor.brake()
        #left_motor.brake()

#speedAmax(SA, 15)


    
