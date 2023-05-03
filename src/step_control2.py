from machine import Pin
import utime
import stepper
import robot
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


mymotortest = stepper.Stepper(pins2,Motorname, Motortype )

pwma = Pin(6, Pin.OUT)
pwmb = Pin(7, Pin.OUT)
pwma.value(1)
pwmb.value(1)
pwma2 = Pin(1, Pin.OUT)
pwmb2 = Pin(2, Pin.OUT)
pwma2.value(1)
pwmb2.value(1)
stby = Pin(8,Pin.OUT)
stby.value(1)
stby2 = Pin(3,Pin.OUT)
stby2.value(1)



#pw_a = Pin(1, Pin.OUT)
# pw_b = Pin(2, Pin.OUT)
# pw_a.value(1)
# pw_b.value(1)
# stby1 = Pin(3,Pin.OUT)
# stby1.value(1)


utime.sleep(1)
input("Press <Enter> to continue Test1")
wait = 0.5
steps = 50 # No of step sequences
ccwise = False
verbose= True
steptype = "full"
initdelay = 1
mymotortest.motor_run(wait = 0.001, verbose=True, steptype='full', ccwise=True, steps=1000000000000)
utime.sleep(1)


utime.sleep(1)
input("Press <Enter> to continue Test2")
wait = 0.1
steps = 25 # No of step sequences
ccwise = False
verbose= True
steptype = "full"
initdelay = 1
mymotortest.motor_run(wait ,steps ,ccwise ,verbose, steptype ,initdelay)
utime.sleep(1)


utime.sleep(1)
input("Press <Enter> to continue Test3")
wait = 0.2
steps = 25 # No of step sequences
ccwise = False
verbose= True
steptype = "half"
initdelay = 1
mymotortest.motor_run(wait ,steps ,ccwise ,verbose, steptype ,initdelay)
utime.sleep(1)

utime.sleep(1)
input("Press <Enter> to continue Test4")
wait = 0.05
steps = 50 # No of step sequences
ccwise = False
verbose= True
steptype = "half"
initdelay = 1
mymotortest.motor_run(wait ,steps ,ccwise ,verbose, steptype ,initdelay)
utime.sleep(1)


