from machine import Pin

step = Pin(2,Pin.OUT)
dir = Pin(3,Pin.OUT)
spr = 4000

while True:
    dir.high()
    for x in range(spr):
        step.high()
        utime.sleep(0.001)

        step.low()
        utime.sleep(0.001)
    
    utime.sleep(2)

    dir.low()

    for j in range(spr):
        step.high()
        utime.sleep(0.001)

        step.low()
        utime.sleep(0.001)
        
    utime.sleep(2)


    