
import machine
from machine import Pin
import utime

class Robot(object):

    def __init__(self, pins, pins_2 ):
        self.stop_motor = False
        self.pins = pins
        self.pins_2 = pins_2
    
    def motor_stop(self):
        self.stop_motor = True
    

    
    def forward(self, wait = 0.001, steps = 512, steptype = 'half', initdelay = 0.001 ):
        
        
        if steps < 0:
            print("StepError: Step number must be greater than 0")
        
        try:
            pins = []
            pins_2 = []
            self.stop_motor = False
            for pin in self.pins:
                pins.append(Pin(pin, Pin.OUT))
            for pin in self.pins_2:
                pins_2.append(Pin(pin,Pin.OUT))
                
            utime.sleep(initdelay)

            # select step based on user input
            # Each step_sequence is a list containing GPIO pins that should be set to High
            if steptype == "half":  # half stepping.
                step_sequence = list(range(0, 8))
                step_sequence[0] = [pins[0]]
                step_sequence[1] = [pins[0] ,pins[1]]
                step_sequence[2] = [pins[1]]
                step_sequence[3] = [pins[1] ,pins[2]]
                step_sequence[4] = [pins[2]]
                step_sequence[5] = [pins[2], pins[3]]
                step_sequence[6] = [pins[3]]
                step_sequence[7] = [pins[3],pins[0]]
            elif steptype == "full":  # full stepping.
                step_sequence = list(range(0, 4))
                step_sequence[0] = [pins[0], pins[1]]
                step_sequence[1] = [pins[1], pins[2]]
                step_sequence[2] = [pins[2], pins[3]]
                step_sequence[3] = [pins[0], pins[3]]
            elif steptype == "wave":  # wave driving
                step_sequence = list(range(0, 4))
                step_sequence[0] = [pins[0]]
                step_sequence[1] = [pins[1]]
                step_sequence[2] = [pins[2]]
                step_sequence[3] = [pins[3]]
            else:
                
                print(steptype)
                quit()

            #  To run motor in reverse we flip the sequence order.
            

            # Iterate through the pins turning them on and off.
            steps_remaining = steps
            while steps_remaining > 0:
                for pin_list in step_sequence:
                    for i,pin in enumerate(pins):
                        if self.stop_motor:
                            print('stop motor interrput')
                            for j,pin in enumerate(pins):
                                 pin.value(0)
                                 pins_2[j].value(0)
                                 
                        else:
                            if pin in pin_list:
                                pin.value(1)
                                pins_2[i].value(1)
                            else:
                                pin.value(0)
                                pins_2[i].value(0)
                    
                    utime.sleep(wait)
                steps_remaining -= 1

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : StepMotorLib: ")
        
        except Exception as motor_error:
            #print(sys.exc_info()[0])
            print(motor_error)
            print("Error : MotorError   : Unexpected error:")
        
            # print report status if everything went well
            
        finally:
            # switch off pins at end
            for i,pin in enumerate(pins):
                pin.value(0)
                pins_2[i].value(0)


    def turn_left(self, wait = 0.001, steps = 512, steptype = 'half', initdelay = 0.001 ):
        if steps < 0:
            print("StepError: Step number must be greater than 0")
        
        try:
            pins = []
            pins_2 = []
            all_pins=[]            
            self.stop_motor = False
            for pin in self.pins:
                pins.append(Pin(pin, Pin.OUT))
            for pin in self.pins_2:
                pins_2.append(Pin(pin,Pin.OUT))
            
            for x,y in enumerate(pins):
                all_pins.append(y)
                all_pins.append(pins_2[x])
                
            utime.sleep(initdelay)

            # select step based on user input
            # Each step_sequence is a list containing GPIO pins that should be set to High
            if steptype == "half":  # half stepping.
                step_sequence = list(range(0, 8))
                step_sequence[0] = [pins[0],pins_2[3], pins_2[0]]
                step_sequence[1] = [pins[0] ,pins[1], pins_2[3]]
                step_sequence[2] = [pins[1],pins_2[2], pins_2[3]]
                step_sequence[3] = [pins[1] ,pins[2],pins_2[2]]
                ####################################
                step_sequence[4] = [pins[2],pins_2[1],pins_2[2]]
                step_sequence[5] = [pins[2], pins[3],pins_2[1]]
                step_sequence[6] = [pins[3],pins_2[0], pins_2[1]]
                step_sequence[7] = [pins[3],pins[0],pins_2[0]]
            elif steptype == "full":  # full stepping.
                step_sequence = list(range(0, 4))
                step_sequence[0] = [pins[0], pins[1]]
                step_sequence[1] = [pins[1], pins[2]]
                step_sequence[2] = [pins[2], pins[3]]
                step_sequence[3] = [pins[0], pins[3]]
            elif steptype == "wave":  # wave driving
                step_sequence = list(range(0, 4))
                step_sequence[0] = [pins[0]]
                step_sequence[1] = [pins[1]]
                step_sequence[2] = [pins[2]]
                step_sequence[3] = [pins[3]]
            else:
                
                print(steptype)
                quit()

            #  To run motor in reverse we flip the sequence order.
            

            # Iterate through the pins turning them on and off.
            steps_remaining = steps
            while steps_remaining > 0:
                for pin_list in step_sequence:
                    for i,pin in enumerate(all_pins):
                        if self.stop_motor:
                            print('stop motor')
                            for j,pin in enumerate(all_pins):
                                pin.value(0)
                        else:
                            if pin in pin_list:
                                pin.value(1)
                            else:
                                pin.value(0)
                
                               
                    utime.sleep(wait)
                steps_remaining -= 1

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : StepMotorLib: ")
        
        except Exception as motor_error:
            #print(sys.exc_info()[0])
            print(motor_error)
            print("Error : MotorError   : Unexpected error:")
        
            # print report status if everything went well
            
        finally:
            # switch off pins at end
            for i,pin in enumerate(pins):
                pin.value(0)
                pins_2[i].value(0)

    def turn_right(self, wait = 0.001, steps = 512, steptype = 'half', initdelay = 0.001 ):
        if steps < 0:
            print("StepError: Step number must be greater than 0")
        
        try:
            pins = []
            pins_2 = []
            all_pins=[]            
            self.stop_motor = False
            for pin in self.pins:
                pins.append(Pin(pin, Pin.OUT))
            for pin in self.pins_2:
                pins_2.append(Pin(pin,Pin.OUT))
            
            for x,y in enumerate(pins):
                all_pins.append(y)
                all_pins.append(pins_2[x])
                
            utime.sleep(initdelay)

            # select step based on user input
            # Each step_sequence is a list containing GPIO pins that should be set to High
            if steptype == "half":  # half stepping.
                step_sequence = list(range(0, 8))
                step_sequence[0] = [pins[0],pins_2[3], pins_2[0]]
                step_sequence[1] = [pins[0] ,pins[1], pins_2[3]]
                step_sequence[2] = [pins[1],pins_2[2], pins_2[3]]
                step_sequence[3] = [pins[1] ,pins[2],pins_2[2]]
                ####################################
                step_sequence[4] = [pins[2],pins_2[1],pins_2[2]]
                step_sequence[5] = [pins[2], pins[3],pins_2[1]]
                step_sequence[6] = [pins[3],pins_2[0], pins_2[1]]
                step_sequence[7] = [pins[3],pins[0],pins_2[0]]
            elif steptype == "full":  # full stepping.
                step_sequence = list(range(0, 4))
                step_sequence[0] = [pins[0], pins[1]]
                step_sequence[1] = [pins[1], pins[2]]
                step_sequence[2] = [pins[2], pins[3]]
                step_sequence[3] = [pins[0], pins[3]]
            elif steptype == "wave":  # wave driving
                step_sequence = list(range(0, 4))
                step_sequence[0] = [pins[0]]
                step_sequence[1] = [pins[1]]
                step_sequence[2] = [pins[2]]
                step_sequence[3] = [pins[3]]
            else:
                
                print(steptype)
                quit()

            #  To run motor in reverse we flip the sequence order.
            
            step_sequence.reverse()
            # Iterate through the pins turning them on and off.
            steps_remaining = steps
            while steps_remaining > 0:
                for pin_list in step_sequence:
                    for i,pin in enumerate(all_pins):
                        if self.stop_motor:
                            print('stop motor')
                            for j,pin in enumerate(all_pins):
                                pin.value(0)
                        else:
                            if pin in pin_list:
                                pin.value(1)
                            else:
                                pin.value(0)
                
                               
                    utime.sleep(wait)
                steps_remaining -= 1

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : StepMotorLib: ")
        
        except Exception as motor_error:
            #print(sys.exc_info()[0])
            print(motor_error)
            print("Error : MotorError   : Unexpected error:")
        
            # print report status if everything went well
            
        finally:
            # switch off pins at end
            for i,pin in enumerate(pins):
                pin.value(0)
                pins_2[i].value(0)




    


