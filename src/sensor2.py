from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340 # Vitesse du son dans l'air
TRIG_PULSE_DURATION_US=10


trig_pin = Pin(4, Pin.OUT) # Broche GP15 de la Pico
echo_pin = Pin(5, Pin.IN)

trig_pin2 = Pin(9,Pin.OUT)
echo_pin2 = Pin(10,Pin.IN)

trig_pin3 = Pin(11,Pin.OUT)
echo_pin3= Pin(18,Pin.IN)





def sens1():
    trig_pin.value(0)
    time.sleep_us(5)
    # Créer une impulsion de 10 µs
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    print(f"Sensor1 : {distance_cm} cm")
    time.sleep_ms(500)
    if(distance_cm<10):
        return 1
    else:
        return 0
def sens2():
    trig_pin2.value(0)
    time.sleep_us(5)
    # Créer une impulsion de 10 µs
    trig_pin2.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin2.value(0)

    ultrason_duration = time_pulse_us(echo_pin2, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    #print(f"Distance : {distance_cm} cm")
    print(f"Sensor2: {distance_cm} cm")
    time.sleep_ms(500)
    if(distance_cm<10):
        return 1
    else:
        return 0
def sens3():
    trig_pin3.value(0)
    time.sleep_us(5)
    # Créer une impulsion de 10 µs
    trig_pin3.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin3.value(0)

    ultrason_duration = time_pulse_us(echo_pin3, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    print(f"Sensor3 : {distance_cm} cm")
    time.sleep_ms(500)
    if(distance_cm<10):
        return 1
    else:
        return 0


while(True):
    print([sens1(),sens2(),sens3()])
  