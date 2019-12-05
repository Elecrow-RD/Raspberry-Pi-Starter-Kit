import RPi.GPIO as GPIO   #import the GPIO library
import time               #import the time library

class Buzzer(object):

    def __init__(self):

        GPIO.setmode(GPIO.BCM)  
        self.buzzer_pin = 17 #set to GPIO pin 17
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        print("buzzer ready")

    def buzz(self,pitch, duration):   #create the function “buzz” and feed it the pitch and duration)

        if(pitch==0):
            time.sleep(duration)
            return 

        period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
        delay = period / 2     #calcuate the time for half of the wave  
        cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency

        for i in range(cycles):    #start a loop from 0 to the variable “cycles” calculated above
            GPIO.output(self.buzzer_pin, True)   #set pin 18 to high
            time.sleep(delay)    #wait with pin 18 high
            GPIO.output(self.buzzer_pin, False)    #set pin 18 to low
            time.sleep(delay)    #wait with pin 18 low

    def play(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        x=0
        pitches=[262,294,330,349,392,440,494,523, 587, 659,698,784,880,988,1047]
        duration=0.1
        for p in pitches:
            self.buzz(p, duration)  #feed the pitch and duration to the function, “buzz”
            time.sleep(duration *0.5)
        for p in reversed(pitches):
            self.buzz(p, duration)
            time.sleep(duration *0.5)

if __name__ == "__main__":
  buzzer = Buzzer()
  buzzer.play()
