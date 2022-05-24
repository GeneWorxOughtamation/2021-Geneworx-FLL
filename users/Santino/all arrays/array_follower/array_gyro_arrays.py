
#Arrays for array gyro program.

#If you are going backwards you must put in lowers values as you go backwards.

#If want to go backwards you must use negative speed.

#Uses zero distance if you want to turn without moving.

#The roll array is used to have the robot brake after it has done a section in the array.
#If the number is 1 then the robot will brake if it it anything but the number 1 then the robot will not brake.

#                   1  2  3   4   5   6   7  8  9 10 11
distance_array= [   2, 0, 30, 0, 44, 55, 64, 72]
speed_array=    [  70,60,100,60,180,120,120,300]
angle_array=    [   0,55, 55, 3,  3,  3, 33, 33]
roll_array=     [   1, 1,  0, 1,  0,  0,  1,  1]