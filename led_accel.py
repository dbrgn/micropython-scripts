"""
Small program to show the acceleration of the x and y axis on the LEDs. The
more you accelerate the board, the more LEDs light up.

An easy way to test this is to hold the board vertically. This causes the
gravity to "pull" on the accelerator – the LEDs light up.

"""
import pyb
import math

leds = [pyb.LED(i) for i in [1, 2, 3, 4]]
ac = pyb.Accel()

def accel():
    """
    Return the maximum absolute acceleration in x or y direction.

    Should return values between 0 and 30.

    """
    vals = [abs(x) for x in [ac.x(), ac.y()]]
    return max(vals)

def show_leds(n):
    """
    Enable n LEDs.

    The parameter n should be in the 1..4 range.

    """
    for i, led in enumerate(leds, 1):
        if i <= n:
            led.on()
        else:
            led.off()

while 1:
    a = accel()
    nof_leds = math.ceil(a / 7.5)
    show_leds(nof_leds)
    pyb.delay(5)
