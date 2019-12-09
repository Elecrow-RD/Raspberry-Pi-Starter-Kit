#!/usr/bin/python
# -*- coding:utf-8 -*-
# www.elecrow.com
import smbus
import time


# NOTE: the PCF8591 script can be used both with photoresistance example and flame sensor example
# please follow up the instructions on the PCF8591 schematic to connect the right sensors in the right way.

address = 0x48

A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43

bus = smbus.SMBus(1)

while True:
    bus.write_byte(address,A0)
    value = bus.read_byte(address)
    print("AOUT:%1.3f  " %(value*3.3/255))
    time.sleep(0.1)
    
