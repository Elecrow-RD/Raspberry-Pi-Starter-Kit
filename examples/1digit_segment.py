import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

# Segment 1 Digit Numbers Illustration
# H Is the dot on the right side of the segment
#         A
#    -----------
#    |         |
#  B |         | C
#    |    D    |
#    -----------
#    |         |
#  E |         | F
#    |         | 
#    ----------- (self.H) 
#         G

class Segment():

    def __init__(self):

        # set the GPIO mode as GPIO.BCM
        GPIO.setmode(GPIO.BCM)
        # set pin names for each of the segment pins
        self.A = 25
        self.B = 20
        self.C = 24
        self.D = 21
        self.E = 16
        self.F = 18
        self.G = 12
        self.H = 23
        # set the segment pins as GPIO.OUT
        GPIO.setup(self.A, GPIO.OUT) 
        GPIO.setup(self.B, GPIO.OUT) 
        GPIO.setup(self.C, GPIO.OUT) 
        GPIO.setup(self.D, GPIO.OUT) 
        GPIO.setup(self.E, GPIO.OUT) 
        GPIO.setup(self.F, GPIO.OUT) 
        GPIO.setup(self.G, GPIO.OUT) 
        GPIO.setup(self.H, GPIO.OUT)

    def hide_number(self):
        # make sure everyone is low
        GPIO.output(self.A,GPIO.LOW)
        GPIO.output(self.B,GPIO.LOW)
        GPIO.output(self.C,GPIO.LOW)
        GPIO.output(self.D,GPIO.LOW)
        GPIO.output(self.E,GPIO.LOW)
        GPIO.output(self.F,GPIO.LOW)
        GPIO.output(self.G,GPIO.LOW)
        GPIO.output(self.H,GPIO.LOW)
        
    def show_number(self,number):
        # make sure to clean the previous numbers before drawing new one
        self.hide_number()
        # check which number to draw and draw it
        if(number == 0):
            # number zero pins: A,B,C,E,F,G
            GPIO.output(self.A,GPIO.HIGH)
            GPIO.output(self.B,GPIO.HIGH)
            GPIO.output(self.C,GPIO.HIGH)
            GPIO.output(self.E,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
            GPIO.output(self.G,GPIO.HIGH)
        elif(number == 1):
            # number one pins: C,F
            GPIO.output(self.C,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
        elif(number == 2):
            # number two pins: A,C,D,E,G
            GPIO.output(self.A,GPIO.HIGH)
            GPIO.output(self.C,GPIO.HIGH)
            GPIO.output(self.D,GPIO.HIGH)
            GPIO.output(self.E,GPIO.HIGH)
            GPIO.output(self.G,GPIO.HIGH)
        elif(number == 3):
            # number three pins: A,C,D,F,G
            GPIO.output(self.A,GPIO.HIGH)
            GPIO.output(self.C,GPIO.HIGH)
            GPIO.output(self.D,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
            GPIO.output(self.G,GPIO.HIGH)
        elif(number == 4):
            # number four pins: B,C,D,F
            GPIO.output(self.B,GPIO.HIGH)
            GPIO.output(self.C,GPIO.HIGH)
            GPIO.output(self.D,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
        elif(number == 5):
            # number five pins: A,B,D,F,G
            GPIO.output(self.A,GPIO.HIGH)
            GPIO.output(self.B,GPIO.HIGH)
            GPIO.output(self.D,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
            GPIO.output(self.G,GPIO.HIGH)
        elif(number == 6):
            # number six pins: A,B,D,E,F,G
            GPIO.output(self.A,GPIO.HIGH)
            GPIO.output(self.B,GPIO.HIGH)
            GPIO.output(self.D,GPIO.HIGH)
            GPIO.output(self.E,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
            GPIO.output(self.G,GPIO.HIGH)
        elif(number == 7):
            # number seven pins: A,C,F
            GPIO.output(self.A,GPIO.HIGH)
            GPIO.output(self.C,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
        elif(number == 8):
            # number eight pins: A,B,C,D,E,G,F
            GPIO.output(self.A,GPIO.HIGH)
            GPIO.output(self.B,GPIO.HIGH)
            GPIO.output(self.C,GPIO.HIGH)
            GPIO.output(self.D,GPIO.HIGH)
            GPIO.output(self.E,GPIO.HIGH)
            GPIO.output(self.G,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
        elif(number == 9):
            # number nine pins: A,B,C,D,F
            GPIO.output(self.A,GPIO.HIGH)
            GPIO.output(self.B,GPIO.HIGH)
            GPIO.output(self.C,GPIO.HIGH)
            GPIO.output(self.D,GPIO.HIGH)
            GPIO.output(self.F,GPIO.HIGH)
        else:
            # if none of the numbers, it's dot. turn on the dot
            GPIO.output(self.H,GPIO.HIGH)

def main():
    # initialize the segment class object
    segment = Segment()
    # for i in range of 0 to 9, show the segment number at i 
    # and wait 1 second before showing the next one
    for i in range(0,10):
        segment.show_number(i)            
        time.sleep(1)
    # when finish, clean up GPIO
    GPIO.cleanup()

main()
