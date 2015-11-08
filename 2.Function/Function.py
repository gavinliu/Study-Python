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


def move(x, y, length=1):
    newX = x + length
    newY = y + length
    return newX, newY

i = move(1, 1, 3)

print i

x, y = move(2, 3, 4)

print x, y

x, y = move(2, 3)

print x, y

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

x = fact(5)

print x

def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

x = fact(1000)

print x
