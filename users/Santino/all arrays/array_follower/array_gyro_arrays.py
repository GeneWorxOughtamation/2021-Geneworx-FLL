
#Arrays for array gyro program.

#If you are going backwards you must put in lowers values as you go backwards.

#If want to go backwards you must use negative speed.

#Uses zero distance if you want to turn without moving.

#The roll array is used to have the robot brake after it has done a section in the array.
#If the number is 1 then the robot will brake if it is 0 then the robot will not brake.

#                   1  2  3   4   5   6   7  8  9 10 11
distance_array= [   2, 0, 33, 0, 44, 55, 60, 72]
speed_array=    [  70,60,200,60,300,250,120,300]
angle_array=    [   0,45, 45, 2,  0,  0, 33, 33]
roll_array=     [   1, 1,  1, 1,  1,  1,  1,  1]

distance_six_feet_test= [ 72]
speed_six_feet_test=    [600]
angle_six_feet_test=    [  0]
roll_six_feet_test=     [  1]