from machine import Pin
import utime
from stepper import Stepper
import _thread

#TODO pins for right motor
#TODO requires fine tuning

l_pins = [13,14,12,15]
l_pwma = Pin(6, Pin.OUT)
l_pwmb = Pin(7, Pin.OUT)
l_stby = Pin(8,Pin.OUT)
l_stby.value(1)
l_pwma.value(1)
l_pwmb.value(1)
##########################
r_pins = [22,20,21,19]
r_pwma = Pin(1,Pin.OUT)
r_pwmb = Pin(2,Pin.OUT)
r_stby = Pin(3,Pin.OUT)
r_stby.value(1)
r_pwma.value(1)
r_pwmb.value(1)

V = Pin(10, Pin.OUT)
V.value(1)



left_motor = Stepper(pins=l_pins, name='left_motor', motor_type='Nema')
right_motor = Stepper(pins = r_pins, name= 'right_motor', motor_type='Nema')



def move_forward1():
    left_motor.motor_run(wait = 0.001, verbose=True, steptype='full', ccwise=True, steps=50)
def move_forward2():
    right_motor.motor_run(wait = 0.001, verbose=True, steptype='full', ccwise=False, steps=50)
    

def turn_left():
    left_motor.motor_run(ccwise=True, wait = 0.5)
    right_motor.motor_run(initdelay=0, wait = 0.5)

def turn_right():
    left_motor.motor_run()
    right_motor.motor_run(ccwise=True, initdelay=0)

def turn_back():
    left_motor.motor_run(ccwise=True)
    right_motor.motor_run(initdelay=0)

def stop():
    left_motor.stop_motor= True
    right_motor.stop_motor=True

def move_half():
    left_motor.motor_run(steps=25)
    right_motor.motor_run(initdelay=0,steps=25)


_thread.start_new_thread(move_forward1,())
move_forward2()




