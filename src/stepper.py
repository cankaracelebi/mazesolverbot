
import machine
from machine import Pin
import utime

class Stepper(object):

    def __init__(self, pins, name='Step1', motor_type = 'Nema', ):
        self.name = name
        self.motor_type = motor_type
        self.stop_motor = False
        self.pins = pins
    
    def motor_stop(self):
        self.stop_motor = True
    

    
    def motor_run(self, wait = 0.001, steps = 512, ccwise = False, verbose = False, steptype = 'half', initdelay = 0.001):
        # pins = int list of pin numbers a in a out b in b out eg: [13,12,14,15]
        # wait: duration between steps
        # default steps for a revolution
        # ccwise = reverses the sequence
        # steptype = 'full'(high torque), 'half step'(medium torque results in smoother revolutions), 'wave'(useless)
        # verbose = just verbose for testing nothing important regarding the actual bot
        # initdelay : wait time before motor's first step
        
        if steps < 0:
            print("StepError: Step number must be greater than 0")
        
        try:
            pins = []
            self.stop_motor = False
            for pin in self.pins:
                pins.append(Pin(pin, Pin.OUT))
                
            utime.sleep(initdelay)

            # select step based on user input
            # Each step_sequence is a list containing GPIO pins that should be set to High
            if steptype == "half":  # half stepping.
                step_sequence = list(range(0, 8))
                step_sequence[0] = [pins[0]]
                step_sequence[1] = [pins[0], pins[1]]
                step_sequence[2] = [pins[1]]
                step_sequence[3] = [pins[1], pins[2]]
                step_sequence[4] = [pins[2]]
                step_sequence[5] = [pins[2], pins[3]]
                step_sequence[6] = [pins[3]]
                step_sequence[7] = [pins[3], pins[0]]
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
                print("Error: StepTypeError : unknown step type : half, full or wave")
                print(steptype)
                quit()

            #  To run motor in reverse we flip the sequence order.
            if ccwise:
                step_sequence.reverse()

            def display_degree():
                """ display the degree value at end of run if verbose"""
                if self.motor_type == "28BYJ":
                    degree = 1.422222
                    print("Size of turn in degrees = {}".format(round(steps/degree, 2)))
                elif self.motor_type == "Nema":
                    degree = 7.2
                    print("Size of turn in degrees = {}".format(round(steps*degree, 2)))
                else:
                    # Unknown Motor type
                    print("Warning 201 : Unknown Motor Type : {}".format(self.motor_type))
                    print("Size of turn in degrees = N/A")

            def print_status(enabled_pins):
                """   Print status of pins."""
                if verbose:
                    print("Next Step: Step sequence remaining : {} ".format(steps_remaining))
                    for pin_print in pins:
                        if pin_print in enabled_pins:
                            print(" pin on {}".format(pin_print))
                        else:
                            print("pin off {}".format(pin_print))

            # Iterate through the pins turning them on and off.
            steps_remaining = steps
            while steps_remaining > 0:
                for pin_list in step_sequence:
                    for pin in pins:
                        if self.stop_motor:
                            print('stop motor interrput')
                            for pin in pins:
                                 pin.value(0)
                        else:
                            if pin in pin_list:
                                pin.value(1)
                            else:
                                pin.value(0)
                    print_status(pin_list)
                    utime.sleep(wait)
                steps_remaining -= 1

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : StepMotorLib: ")
        
        except Exception as motor_error:
            #print(sys.exc_info()[0])
            print(motor_error)
            print("Error : MotorError   : Unexpected error:")
        else:
            # print report status if everything went well
            if verbose:
                print("\nStepMotorLib, Motor Run finished, Details:.\n")
                print("Motor type = {}".format(self.motor_type))
                print("Initial delay = {}".format(initdelay))
                print("Used pins = {}".format(pins))
                print("Wait time = {}".format(wait))
                print("Number of step sequences = {}".format(steps))
                print("Size of step sequence = {}".format(len(step_sequence)))
                print("Number of steps = {}".format(steps*len(step_sequence)))
                display_degree()
                print("Counter clockwise = {}".format(ccwise))
                print("Verbose  = {}".format(verbose))
                print("Steptype = {}".format(steptype))
        finally:
            # switch off pins at end
            for pin in pins:
                pin.value(0)
    


