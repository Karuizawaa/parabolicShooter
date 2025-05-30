#!/usr/bin/env python
import matplotlib.pyplot as plt
import math
import numpy as np

GRAVITY = 9.80665 #m/s
ANGLE = 45 #degree elevation

def toRad(degree):
    return degree * math.pi / 180

def vshoot(x, y):
    plt.scatter(x, y, color='r', label='Target (tiang)')
    plt.text(x+0.1, y+0.1, "(" + str(x) + ", " + str(y) + ")")
    initVel = math.sqrt((GRAVITY * (x ** 2)) / ((math.tan(toRad(ANGLE)) * x - y) * 2 * (math.cos(toRad(ANGLE)) ** 2)))
    if initVel > 6500:
        return 0
    else:
        return initVel

def plot(initVel):
    plt.title("Trajektori penembak ANGLE")
    d = np.arange(0, (initVel ** 2) * math.sin(toRad(2*ANGLE)) / GRAVITY , 0.001)
    h = math.tan(toRad(ANGLE)) * d - (GRAVITY * (d ** 2) / (2 * ((initVel * math.cos(toRad(ANGLE))) ** 2 )))
    plt.text(0, 0, str(initVel) + " m/s")
    plt.plot(d, h, color='b', label='Trajektori')
    plt.title("Trajektori penembak sudut " + str(ANGLE) + "°")
    plt.legend()
    plt.axis('equal')
    plt.show()

plot(vshoot(4,3)) #metric (m) unit brok (x,y) / x for horizontal distance, y for vertical distance
