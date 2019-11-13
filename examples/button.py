#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# configure both button and buzzer pins
button_pin = 17

# set board mode to GPIO.BOARD
GPIO.setmode(GPIO.BCM)

# setup button pin asBu input and buzzer pin as output
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # check if button pressed
        if(GPIO.input(button_pin) == 0):
            # Button is pressed
            print("Button Pressed")
        else:
            # it's not pressed
            print("Button Released")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
