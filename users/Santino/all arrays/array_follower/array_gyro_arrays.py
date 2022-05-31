
#Arrays for array gyro program.

#If you are going backwards you must put in lowers values as you go backwards.

#If want to go backwards you must use negative speed.

#Uses zero distance if you want to turn without moving.

#The roll array is used to have the robot brake after it has done a section in the array.
#If the number is 1 then the robot will brake if it is 0 then the robot will not brake.

#The gyro will work better if when turning have your robot turn at the able you want but when you want to move after that then have the robot go at a angle slightly less than the turned angle.
#For example if you have the robot turn 45 degrees then once the robot starts to move forward have it move at angle slightly less than 45 degrees for example 43 or 44.

#                   1  2  3   4   5   6   7  8  9 10 11
distance_array= [   2, 0, 29, 0, 44, 55, 57, 74]
speed_array=    [  70,60,370,60,400,400,200,400]
angle_array=    [   0,45, 43, 2,  0,  0, 33, 33]
roll_array=     [   1, 1,  1, 1,  1,  1,  1,  1]

distance_six_feet_test= [ 72]
speed_six_feet_test=    [600]
angle_six_feet_test=    [  0]
roll_six_feet_test=     [  1]