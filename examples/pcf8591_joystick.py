#!/usr/bin/python
# -*- coding:utf-8 -*-
# www.elecrow.com
import smbus
import time


# NOTE: This PCF8591 script is used with the joystick example because we will need to use more than 1 analog input
# please follow up the instructions on the PCF8591 schematic to connect the right sensors in the right way.

address = 0x48

A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43

bus = smbus.SMBus(1)

while True:
    # get value X
    bus.write_byte(address,A0)
    value_x = bus.read_byte(address)
    # get value Y
    bus.write_byte(address,A1)
    value_y = bus.read_byte(address)
    # get value Z
    bus.write_byte(address,A2)
    value_z = bus.read_byte(address)
    # print the values
    print("Value X: %s" % value_x)
    print("Value Y: %s" % value_y)
    print("Value Z: %s" % value_z)
    time.sleep(0.1)
