"""Created by Ihor Chernyshev"""
"""Created on Feb 2025"""
"""This program blinks the built-in LED"""

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
