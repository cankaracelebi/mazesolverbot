import random
from machine import Pin
import machine
import utime
from robot import Robot
import sensor


pins1 = [13,12,14,15]
pins2 = [22,21,20,19]
##########################################
pwma = Pin(6, Pin.OUT)
pwmb = Pin(7, Pin.OUT)
pwma.value(1)
pwmb.value(1)
pwma2 = Pin(0, Pin.OUT)
pwmb2 = Pin(2, Pin.OUT)
pwma2.value(1)
pwmb2.value(1)
stby = Pin(8,Pin.OUT)
stby.value(1)
stby2 = Pin(3,Pin.OUT)
stby2.value(1)
#########################################

myrobot = Robot(pins1,pins2)

# This is the dictionary that we save values of cells.
cell_values={}
path = []
# i will record every move of the robot and filter throught the simplification algorithm, if allowed we could put the robot to the start otherwise i will let it go back to the origin 
# and solve it with the shortest path
# Using x and y for save location of robot.
x=0
y=0
#The sensors return a HIGH signal if there is no object within the threshold distance and a LOW signal if there is an object within this distance.
# Right-Forward-Left. This is the order that I use from index 0 to 2. 
#sensors=[right,center,left] 
# This is the first direction of robot. I named directions as north,south,east, and west.
# But they are doesn't have to equal to real life.
dir= "North"
# This dictionary will help us at checking what is the location if robot turns right,left or move forward.
# Also will help us at updating coordinates. 
next_loc_count={
    "North":{"Left":[-1,0],"Right":[1,0],"Forward":[0,1]},
    "South":{"Left":[1,0],"Right":[-1,0],"Forward":[0,-1]},
    "West":{"Left":[0,-1],"Right":[0,1],"Forward":[-1,0]},
    "East":{"Left":[0,1],"Right":[0,-1],"Forward":[1,0]}
}
# This dictionary will help us at updating robot's direction depending on robot's move, and former direction.
dir_update={
    "North":{"Back":"South","Right":"East","Left":"West","Forward":"North"},
    "South":{"Back":"North","Right":"West","Left":"East","Forward":"South"},
    "West":{"Back":"East","Right":"North","Left":"South","Forward":"West"},
    "East":{"Back":"West","Right":"South","Left":"North","Forward":"East"}
}
# This function will help us at finding open roads depending on datas that come from sensors.
def open_roads():
    _open_roads=[]
    if sensor.sens1()==1:
        #right sensor
        _open_roads.append("Right")
    if sensor.sens2()==1:
        #center sensor
        _open_roads.append("Forward")
    if sensor.sens3()==1:
        #left sensor
        _open_roads.append("Left")
    return _open_roads
# This function will help us at checking values of open roads, 
# and if this location's value equal the value that we are looking for adds the way to a list.
def value_checker(value):
    ways=[]
    for road in list(open_roads()):
        next_loc=(x+next_loc_count[dir][road][0],y+next_loc_count[dir][road][1])
        try:
           if cell_values[next_loc]==value:
               ways.append(road)
        except:
            if value==0:
                ways.append(road)
            else:
                pass
    return ways
# This is the function that commands robot to move right,left, or forward.
# Print parts are only for show.
def move(road):
    if road=="Forward":
        #TODO find the required steps
        # move one step
        myrobot.forward(steps=50)
        print("Moving")
    elif road=="Right":
        #TODO find the requiredsteps
        myrobot.turn_right()
        myrobot.forward(steps=50)
            # rotate -90 degree
            # move one step
        print("Right")
    elif road=="Left":
        myrobot.turn_left()
        myrobot.forward(steps=50)
        # rotate 90 degree
        # move one step
        print("Left")

# This is the function that commands robot to turn back.
# We will call it when we are in a dead end.
def turn_back():
    # rotate 180 degree
    myrobot.turn_back()
    dir=dir_update[dir]["Back"]

while True:
    # If we don't have any open roads,which means we are in a dead-end, we are turning back.
    if len(open_roads())==0:
        turn_back()
        dir=dir_update[dir]["Back"]
    # If we have only one open road, we are following it without checking it's value.
    # After this step we are updating our location(x,y), direction, and dictionary that keeping values of cells  .
    # First we're trying to increase value of the cell by 1.
    # If we get an error, that means that we never visited that cell.
    # So we need to add this cell to the dictionary not update it. 
    elif len(open_roads())==1:
        move(open_roads()[0])
        x=x+next_loc_count[dir][open_roads()[0]][0]
        y=y+next_loc_count[dir][open_roads()[0]][1]
        dir=dir_update[dir][open_roads()[0]]
        try:
            cell_values.update({(x,y):cell_values[(x,y)]+1})
        except:
            cell_values.update({(x,y):1})
    # If we have more than 1 open roads, we are checking the values of the cells on those roads.
    elif len(open_roads())>1:
        # First we are checking is there any cell with value 0.
        # If there is cell or cells with value 0 we're randomly choosing one of this roads and follow it.
        # After that, we are updating our location(x,y), direction, and dictionary that keeping values of cells. 
        if len(value_checker(0))>0:
            road_to_go=random.choice(value_checker(0))
            move(road_to_go)
            x=x+next_loc_count[dir][road_to_go][0]
            y=y+next_loc_count[dir][road_to_go][1]
            dir=dir_update[dir][road_to_go]
            try:
                cell_values.update({(x,y):cell_values[(x,y)]+1})
            except:
                cell_values.update({(x,y):1})                     
        # If there is not, we're looking a cell with value 1.
        # If there is cell or cells with value 1 we're randomly choosing one of this roads and follow it.
        # After that, we are updating our location(x,y), direction, and dictionary that keeping values of cells. 
        elif len(value_checker(1))>0:
            road_to_go=random.choice(value_checker(1))
            move(road_to_go)
            x=x+next_loc_count[dir][road_to_go][0]
            y=y+next_loc_count[dir][road_to_go][1]
            dir=dir_update[dir][road_to_go]
            try:
                cell_values.update({(x,y):cell_values[(x,y)]+1})
            except:
                cell_values.update({(x,y):1})                 
        # If there is no cells with value 0 or 1 we're looking a cell with value 2.
        # If there is cell or cells with value 2 we're randomly choosing one of this roads and follow it.
        # After that, we are updating our location(x,y), direction, and dictionary that keeping values of cells. 
        elif len(value_checker(2))>0:
            road_to_go=random.choice(value_checker(2))
            move(road_to_go)
            x=x+next_loc_count[dir][road_to_go][0]
            y=y+next_loc_count[dir][road_to_go][1]
            dir=dir_update[dir][road_to_go]
            try:
                cell_values.update({(x,y):cell_values[(x,y)]+1})
            except:
                cell_values.update({(x,y):1})
 


