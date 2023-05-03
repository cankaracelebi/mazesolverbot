from machine import Pin
import utime
#import stepper
import stepper_2
#https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/Nema11TB6612FNG.md
Motorname = "MotorOne" 
Motortype = "Nema"


A11 = 13
A12 = 12
B11 = 14
B12 = 15

A11_ = 22
A12_ = 21
B11_ = 20
B12_ = 19

V = Pin(10, Pin.OUT)
V.value(1)
V2 = Pin(11, Pin.OUT)
V2.value(1)


GpioPins = [A11, B11, A12, B12]
pins2 = [A11_, B11_, A12_, B12_]


#mymotortest = stepper.Stepper(GpioPins,Motorname, Motortype )
motortest = stepper_2.Robot(GpioPins,pins2)

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


motortest.forward(steps=200)