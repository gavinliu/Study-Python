#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'HelloWorld'

print '你好', '中国'

name = raw_input()
print 'Hello', name

age = raw_input('Please enter your age: ')
print 'Your age is', age

print True and True
print True or False
print not True

names = ['A', 'B', 'C']
for name in names:
    print name

sum = 0
for x in range(101):
    sum = sum + x
print sum
