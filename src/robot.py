from stepper import Stepper
import _thread
import uasyncio as asyncio



class Robot:
    def __init__(self, motor1:Stepper,  motor2:Stepper):
        self.motor1 = motor1
        self.motor2 = motor2
    
    def rotate_one(self):
        self.motor1.motor_run()
        
    def c_rotate_one(self):
        self.motor1.motor_run(ccwise=True)
    def rotate_two(self):
        self.motor2.motor_run()
    def c_rotate_two(self):
        self.motor2.motor_run(ccwise=False)

    def rotate_one_half(self):
        self.motor1.motor_run(steps=1024)
    

        



    def move_forward(self):
        _thread.start_new_thread()
        
        
    



    def turn_left(self):
        return None


    def turn_right(self):
        return None


    def turn_back(self):
        return None


    def stop(self):
        return None
    

    def move_half(self):
        return None
