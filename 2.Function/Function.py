#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def myClamp(x, y):
    if x > y:
        return x
    else:
        return y

i = myClamp(1, 2)

print i


def mySine(angle):
    return math.sin(angle)

i = mySine(math.pi / 6)

print i


def move(x, y, length):
    newX = x + length
    newY = y + length
    return newX, newY

i = move(1, 1, 3)

print i

x, y = move(2, 3, 4)

print x, y
