#found on github, edited by Meghan Sills

from roboclaw import Roboclaw
from time import sleep

roboclaw = Roboclaw("/dev/roboclaw", 38400)
roboclaw.Open()


# Read encoder 1
motor_1_count = roboclaw.ReadEncM1(0x80)
print "Original encoder 1:"
print motor_1_count


# Set encoder and then read and print to test operation
roboclaw.SetEncM1(0x80, 10000)
motor_1_count = roboclaw.ReadEncM1(0x80)
print "After setting count:"
print motor_1_count


# Reset encoders and read and print value to test operation
roboclaw.ResetEncoders(0x80)
motor_1_count = roboclaw.ReadEncM1(0x80)
print "After resetting:"
print motor_1_count


#read encoder 2: 
motor_2_count = roboclaw.ReadEncM2(0x80)
print "Original encoder 2:"
print motor_2_count


#set encoder 2
roboclaw.SetEncM2(0x80, 10000)
motor_2_count = roboclaw.ReadEncM2(0x80)
print "After setting count:"
print motor_2_count


#reset encoder 2 
roboclaw.ResetEncoders(0x80)
motor_2_count = roboclaw.ReadEncM2(0x80) #fixed problem
print "After resetting:"
print motor_2_count

answer = raw_input("Type D to enter a distance or Enter to use excel " )
if (answer == 'D'):
	val = 3.958*input("Enter distance in degrees here: ")
	print("raw val ", val)
	val = round(val)
	val = int(val)
	roboclaw.SpeedAccelDistanceM1(0x80, 500, 50000, val, 1)

else
	import pandas as pd 
	df = pd.read_csv('lensproject.csv', index_col=0)
	position = 19.45*df['position'] #7000/360=19.45
	position = round(position)
	position = int(position)
	
	roboclaw.SpeedAccelDeccelPositionM1(0x80, 5000, 10000, 10000, position, 1) 
	#not sure if correct 7000=1 rev
	


#below is examples of the types of functions we tried with notes 


#operating individual motors
#roboclaw.ForwardM1(0x80, 63) #makes motor run forward at half speed
#sleep(5)
#roboclaw.BackwardM1(0x80, 63) #makes motor run backwards at half speed 
#sleep(5) #after this command, motor just keeps running until unplugged
#roboclaw.ForwardM1(0x80, 0) #stops motor 
#roboclaw.ForwardM2(0x80, 63)
#sleep(5)
#roboclaw.BackwardM2(0x80, 63)
#sleep(5)
#roboclaw.ForwardM2(0x80, 0)


#distance functions 
#roboclaw.SpeedDistanceM1(0x80, 500, 1425, 1) #working now 
#roboclaw.SpeedDistanceM2(0x80, 1000, 1000, 1) #works!!

#roboclaw.SpeedAccelDistanceM1(0x80, 300000, 5000, 356, 1) #trying to find 1 rev 
#roboclaw.SpeedAccelDistanceM2(0x80, 500, 50000, 1425, 1) #works for 1 rev but slow 
#roboclaw.SpeedAccelDistanceM2(0x80, 500, 50000, 79, 1) # 20 degrees exactly 

#roboclaw.SpeedAccelDeccelPositionM1(0x80, 5000, 10000, 10000, 7000, 1) working position function 


#Position Functions 
#try:
	#roboclaw.SpeedAccelDeccelPositionM1(0x80,1000,2000,1000,150000,1) #works now but fails after 
#except OSError as e:
            #print "error"
            #print e
#print "finished"
