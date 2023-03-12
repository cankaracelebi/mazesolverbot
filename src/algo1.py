from machine import Pin
import utime
from stepper import Stepper
import _thread
import motor_functions

left = Pin(19, Pin.IN, Pin.PULL_DOWN )
center = Pin(20, Pin.IN, Pin.PULL_DOWN)
right = Pin(21, Pin.IN, Pin.PULL_DOWN)




#The sensors return a HIGH signal if there is no object within the threshold distance and a LOW signal if there is an object within this distance.
#returns 0 if there's a wall
#left.value() == 0 if there's a wall.

def move_half_size(steps):
    #function to make the robot move half its size
    return None

def check_roads(l=left.value(), c=center.value(), r=right.value()):
    #there are 8 different scenarios to detect
    #l -> left.value()
    if l==0 and c==0 and r == 0:
        #dead end
        return 'D'
    elif l == 0 and c==1 and r ==1:
        #straight or right

        return 'SR'
    elif l==1 and c== 1 and r==0:
        #straight or left
        return 'LS'

    elif l==1 and c==1 and r==1:
        #cross
        return 'LSR'
    elif l==1 and c== 0 and r==1:
        #T shape
        return 'LR'
    elif l==0 and c==0 and r==1:
        #right only
        return 'R'
    elif l==1 and c==0 and r==0:
        #left only
        return 'L'



    #main loop here for the algorithm 
while True:
    state = check_roads()
    
    
        
    

    
