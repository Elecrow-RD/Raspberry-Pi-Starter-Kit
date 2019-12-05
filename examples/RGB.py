#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://elecrow.com/

import time, sys
import RPi.GPIO as GPIO

class RGB():

  # set GPIO mode as GPIO.BOARD
  GPIO.setmode(GPIO.BCM)

  def __init__(self):
      # define the RGB pins
      self.blue = 22
      self.red = 17
      self.green = 27

      # setup the LED pins as output
      GPIO.setup(self.blue, GPIO.OUT)
      GPIO.setup(self.red, GPIO.OUT)
      GPIO.setup(self.green, GPIO.OUT)
      
  def turn_on(self, color):
      if(color == "red"):
          GPIO.output(self.red, GPIO.HIGH)
      if(color == "blue"):
          GPIO.output(self.blue, GPIO.HIGH)
      if(color == "green"):
          GPIO.output(self.green, GPIO.HIGH)
      if(color == "yellow"):
          GPIO.output(self.red, GPIO.HIGH)
          GPIO.output(self.green, GPIO.HIGH)
      if(color == "cyan"):
          GPIO.output(self.blue, GPIO.HIGH)
          GPIO.output(self.red, GPIO.HIGH)
      if(color == "magneta"):
          GPIO.output(self.red, GPIO.HIGH)
          GPIO.output(self.blue, GPIO.HIGH)
      if(color == "white"):
          GPIO.output(self.red, GPIO.HIGH)
          GPIO.output(self.greenb, GPIO.HIGH)
          GPIO.output(self.blue, GPIO.HIGH)
          
  def turn_off(self, color):
      if(color == "red"):
          GPIO.output(self.red, GPIO.LOW)
      if(color == "blue"):
          GPIO.output(self.blue, GPIO.LOW)
      if(color == "green"):
          GPIO.output(self.green, GPIO.LOW)
      if(color == "yellow"):
          GPIO.output(self.red, GPIO.LOW)
          GPIO.output(self.green, GPIO.LOW)
      if(color == "cyan"):
          GPIO.output(self.blue, GPIO.LOW)
          GPIO.output(self.red, GPIO.LOW)
      if(color == "magneta"):
          GPIO.output(self.red, GPIO.LOW)
          GPIO.output(self.blue, GPIO.LOW)
      if(color == "white"):
          GPIO.output(self.red, GPIO.LOW)
          GPIO.output(self.greenb, GPIO.LOW)
          GPIO.output(self.blue, GPIO.LOW)


def main():
    # Initialize RGB Class
    RGB_LED = RGB()
    
    # Blink Red
    RGB_LED.turn_on("red")
    time.sleep(0.3)
    RGB_LED.turn_off("red")
    time.sleep(0.3)
    
    # Blink Green
    RGB_LED.turn_on("green")
    time.sleep(0.3)
    RGB_LED.turn_off("green")
    time.sleep(0.3)
    
    # Blink Blue
    RGB_LED.turn_on("blue")
    time.sleep(0.3)
    RGB_LED.turn_off("blue")

main()
