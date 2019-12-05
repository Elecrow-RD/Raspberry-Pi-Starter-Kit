#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# configure button pin
ball_switch_pin = 17

# set board mode to GPIO.BCM
GPIO.setmode(GPIO.BCM)

# setup ball pin input
GPIO.setup(ball_switch_pin, GPIO.IN)

try:
    while True:
        # check ball state
        if(GPIO.input(ball_switch_pin)):
            # Ball is high means it's closing the circuit by touching
            print("Ball is HIGH")
        else:
            # Ball is low means it's not closing the circuit
            print("Ball is LOW")
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
