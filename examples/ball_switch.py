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
GPIO.setup(ball_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # check ball state
        if(ball_switch_pin):
            # Ball is high means on
            print("Ball is on")
        else:
            # Ball is low means off
            print("Ball is off")
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
