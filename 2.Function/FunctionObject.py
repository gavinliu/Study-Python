#!/usr/bin/env python
# -*- coding: utf-8 -*-

func = lambda x,y: x + y
print func(3,4)


def test(f, a, b):
    print 'test'
    print f(a, b)

test(func, 3, 5)

test((lambda x,y: x**2 + y), 6, 9)

re = map((lambda x,y: x+3 + y ),[1,3,5,6], [1,3,5,6])
print re

print reduce((lambda x,y: x+y),[1,2,5,7,9])


def func(a):
    if a > 100:
        return True
    else:
        return False

print filter(func,[10,56,101,500])

import Function


i = Function.myClamp(1, 2)

print i
