#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import RPi.GPIO as GPIO
import time

# define relay pin
relay_pin = 17

# set GPIO mode as GPIO.BCM
GPIO.setmode(GPIO.BCM)
# setup relay pin as OUTPUT
GPIO.setup(relay_pin, GPIO.OUT)

# Open Relay
GPIO.output(relay_pin, GPIO.HIGH)
# Wait half a second
time.sleep(0.5)
# Close Relay
GPIO.output(relay_pin, GPIO.LOW)
# Wait half a second
time.sleep(0.5)

# Cleanup GPIO pins
GPIO.cleanup()
