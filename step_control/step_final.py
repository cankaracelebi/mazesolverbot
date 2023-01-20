from machine import Pin
import utime

pins = [
    Pin(13, Pin.OUT), # black a in
    Pin(12, Pin.OUT), # green a out,
    Pin(14, Pin.OUT), # Red b in
    Pin(15, Pin.OUT), # blue b out
    ]
pwma = Pin(6, Pin.OUT)
pwmb = Pin(7, Pin.OUT)
pwma.value(1)
pwmb.value(1)
stby = Pin(8,Pin.OUT)
stby.value(1)

full_seq = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
    ]

while True:
    for step in full_seq:
        for j in range(len(pins)):
            pins[j].value(step[j])
            utime.sleep(0.001)
            
'''
phases = [ 1, 5, 4, 6, 2, 10, 8, 9 ]

while True:
    for phase in phases:
        for n, p in enumerate(pins):
            pins[n](phase & 1<<n)
        utime.sleep(0.001)
'''
            
