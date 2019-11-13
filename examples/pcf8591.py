#!/usr/bin/python
# -*- coding:utf-8 -*-
# www.elecrow.com
import smbus
import time

# NOTE: the PCF8591 script can be used both with photoresistance example and flame sensor example
# please follow up the instructions on the PCF8591 schematic to connect the right sensors in the right way.

address = 0x48
cmd = 0x40
value = 0

bus = smbus.SMBus(1)
while True:
    bus.write_byte_data(address,cmd,value)
    value += 1
    if value == 256:
        value =0
    print("AOUT:%3d" %value)
    time.sleep(0.01)
