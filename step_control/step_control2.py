from machine import Pin
import utime

step_one = Pin(2,Pin.OUT)
direction_one = Pin(3,Pin.OUT)
step_two = Pin(8,Pin.OUT)
direction_two = Pin(9, Pin.OUT)
spr = 4000

while True:
    direction_one.high()
    direction_two.high()
    for i in range(spr):
        step_one.high()
        step_two.high()

        utime.sleep(0.001)

        step_one.low()
        step_two.low()

        utime.sleep(0.001)
    utime.sleep(2)
    direction_one.high()
    direction_two.high()

    for j in range(spr):
        step_one.high()
        step_two.high()
        
        
        
        utime.sleep(0.001)

        step_one.low()
        step_two.low()

        utime.sleep(0.001)
    utime.sleep(2)


