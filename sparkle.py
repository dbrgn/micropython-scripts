"""
Turn the LEDs on/off sequentially.
"""
import pyb

leds = [pyb.LED(i) for i in [1, 2, 3, 4]]

def sparkle(delay):
    for led in leds:
        led.on()
        pyb.delay(delay)
    for led in leds:
        led.off()
        pyb.delay(delay)

while 1:
    sparkle(60)
