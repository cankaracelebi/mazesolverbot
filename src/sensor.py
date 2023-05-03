from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340
TRIG_PULSE_DURATION_US=10

#RIGHT
trig1 = Pin(4, Pin.OUT)
echo1 = Pin(5, Pin.OUT)
#CENTER
trig2 = Pin(9, Pin.OUT)
echo2 = Pin(10, Pin.OUT)
#RIGHT
trig3 = Pin(11, Pin.OUT)
echo3 = Pin(18, Pin.OUT)


def sens1():
    #RIGHT
    global trig1,echo1
    
    trig1.value(0)
    time.sleep_us(5)

    trig1.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig1.value(0)

    ultrason_duration = time_pulse_us(echo1, 1, 30000) 
    distance_cm = SOUND_SPEED * ultrason_duration / 20000
    if (distance_cm>=15):
        return 1
    else:
        return 0



def sens2():
    #CENTER
    global trig2,echo2
    trig2.value(1)
    time.sleep_us(5)

    trig2.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig2.value(0)

    ultrason_duration = time_pulse_us(echo2, 1, 30000) 
    distance_cm = SOUND_SPEED * ultrason_duration / 20000
    if (distance_cm>=15):
        return 1
    else:
        return 0


def sens3():
    #LEFT
    global trig3,echo3
    trig3.value(1)
    time.sleep_us(5)

    trig3.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig3.value(0)

    ultrason_duration = time_pulse_us(echo3, 1, 30000) 
    distance_cm = SOUND_SPEED * ultrason_duration / 20000
    if (distance_cm>=15):
        return 1
    else:
        return 0


