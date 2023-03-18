from machine import Pin
from utime import sleep_ms
ir=Pin(21,Pin.IN)
led=Pin(25,Pin.OUT)
while True:
    try:
        if ir.value()==1:
            led.value(0)
        elif ir.value()==0:
            led.value(1)
        sleep_ms(50)
    except KeyboardInterrupt:
        breakS