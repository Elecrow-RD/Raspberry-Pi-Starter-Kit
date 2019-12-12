#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import Adafruit_CharLCD as LCD

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

try:
    while True:
    # Turn backlight on
    lcd.set_backlight(0)
    # clean the LCD screen
    lcd.clear()
    lcd.message('Hello world')
    time.sleep(5)
except KeyboardInterrupt:
    # Turn the screen off
    lcd.clear()
    lcd.set_backlight(1)
