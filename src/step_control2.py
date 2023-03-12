from machine import Pin
import utime
import stepper

Motorname = "MotorOne" 
Motortype = "Nema"

A11 = 13
A12 = 12
B11 = 14
B12 = 15 
GpioPins = [A11, B11, A12, B12]

mymotortest = stepper.Stepper(GpioPins,Motorname, Motortype )

pwma = Pin(6, Pin.OUT)
pwmb = Pin(7, Pin.OUT)
pwma.value(1)
pwmb.value(1)
stby = Pin(8,Pin.OUT)
stby.value(1)

utime.sleep(1)
input("Press <Enter> to continue Test1")
wait = 0.5
steps = 50 # No of step sequences
ccwise = False
verbose= True
steptype = "full"
initdelay = 1
mymotortest.motor_run(verbose=True, steptype='wave', ccwise=True, steps=1000
                      )
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


