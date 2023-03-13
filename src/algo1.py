from machine import Pin
import utime
from stepper import Stepper
import _thread
import motor_functions

left = Pin(19, Pin.IN, Pin.PULL_DOWN )
center = Pin(20, Pin.IN, Pin.PULL_DOWN)
right = Pin(21, Pin.IN, Pin.PULL_DOWN)
#TODO requires fine tuning for IR and motor functions for a fully functional algorithm

path = []


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
    elif l==0 and c==1 and r==0:
        return 'S'
    elif l==1 and c==1 and r ==1:
        return 'END'



def rec_interstection(act,path)->list:
    path.append(act)
    path = simplify_path(path)
    return path


def simplify_path(path)->list:

    #credit to Patrick McCabe
    if len(path<3) or path[-2] != 'B':
        return path

    total_angle = 0
    for i in range(1,4):
        if path[-i] == 'R':
            total_angle += 90
        elif path[-i]=='L':
            total_angle += 270
        elif path[-i] == 'B':
            total_angle += 180
    
    total_angle = total_angle % 360

    if total_angle == 0:
        path[-3] = 'S'
    elif total_angle == 90:
        path[-3] = 'R'
    elif total_angle == 180:
        path[-3] = 'B'
    elif total_angle == 270:
        path[-3] = 'L'
    
    path = path[:-2]
    return path



        

inMaze = True
    #main loop here for the algorithm 
while inMaze:

    state = check_roads()
    if state == 'S':
        motor_functions.move_forward()
    
    elif state == 'D':
        motor_functions.turn_back()
        path = rec_interstection('B', path)

    elif state == 'SR':
        motor_functions.move_half()
        state = check_roads()
        if state == 'SR':
            motor_functions.move_forward()
            path = rec_interstection('S', path)
        else:
            motor_functions.turn_right()
            path = rec_interstection('R', path)
        
    elif state == 'LS':
        motor_functions.move_half()
        motor_functions.turn_left()
        motor_functions.move_forward()
        path = rec_interstection('L', path)
    elif state == 'LSR':
        motor_functions.move_half()
        motor_functions.turn_left()
        motor_functions.move_forward()
        path = rec_interstection('L', path)
    elif state == 'LR':
        motor_functions.move_half()
        motor_functions.turn_left()
        motor_functions.move_forward()
        path = rec_interstection('L', path)
    elif state == 'R':
        motor_functions.move_half()
        motor_functions.turn_left()
        motor_functions.move_forward()
        path = rec_interstection('R', path)
    elif state == 'END':
        inMaze = False
    

goToStart = True
#TODO two loops remanining not necessarily important at the moment

#while goToStart:

#while solveOptimized




    
    
        
    

    
