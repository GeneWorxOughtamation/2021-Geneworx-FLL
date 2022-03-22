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
     rd=robot.distance()
     d=abs(dist) 
     si=0.2*smax
     x=0.20*d
     y=0.8*d
     mi=(smax-si)/x
     md=smax/(y-d)
     if abs(rd) <x:
         s=si+mi*abs(rd)
     if abs(rd)>=x and abs(rd)<=y:
         s=smax
     if abs(rd) >=y and abs(rd)<=d:
         s=md*(abs(rd)-d)+si
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
    #  what's in the paranthesis in the order shown above.
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

gyrom(20,30,200)
gyrom(20,-30,200)
gyrom(-40,0,200)





















    
          