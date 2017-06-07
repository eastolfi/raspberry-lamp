#!/usr/bin/env python

import time
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.2)

width,height=unicorn.get_shape()

def setColor(red, green, blue):
    for x in range(width):
        for y in range(height):
            unicorn.set_pixel(x, y, red, green, blue)

    unicorn.show()

#setColor(255, 0, 0)
#time.sleep(2)
#setColor(0, 255, 0)
#time.sleep(2)
#setColor(0, 0, 255)
#time.sleep(2)
#time.sleep(2)

#time.sleep(2)
setColor(255, 0, 255)
time.sleep(1)
unicorn.brightness(1)
unicorn.show()
#time.sleep(2)
#unicorn.brightness(1)
time.sleep(5)
unicorn.off()

