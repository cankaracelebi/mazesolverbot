import utime
from machine import Pin
import _thread
from stepper import Stepper



l_pins = [12,13,14,15]
r_pins = [5,4,6,7]
l_pwma = Pin(6, Pin.OUT)
l_pwmb = Pin(7, Pin.OUT)
l_stby = Pin(8,Pin.OUT)
l_stby.value(1)
l_pwma.value(1)
l_pwmb.value(1)
r_pwma = Pin(0,Pin.OUT)
r_pwmb = Pin(0,Pin.OUT)
r_stby = Pin(0,Pin.OUT)
r_stby.value(1)
r_pwma.value(1)
r_pwmb.value(1)


left_motor = Stepper(pins=l_pins, name='left_motor', motor_type='Nema')
right_motor = Stepper(pins = r_pins, name= 'right_motor', motor_type='Nema')


def move_forward():
    _thread.start_new_thread(left_motor.motor_run,steps=25)
    _thread.start_new_thread(right_motor.motor_run)

