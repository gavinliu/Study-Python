#!/usr/bin/env python
# -*- coding: utf-8 -*-

for a in [3, 4, 6]:
	print a

idx = range(12)
print idx

for a in idx:
    print a*a

S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# min max length
for i in range(1, len(idx), 2):
    print idx[i]

for (index,char) in enumerate(S):
    print index, " - ", char

ta = [1,2,3]
tb = [9,8,7]

# cluster
zipped = zip(ta,tb)
print(zipped)

# decompose
na, nb = zip(*zipped)
print(na, nb)

file = open("csz.py")

for f in file:
    print f


def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

for i in gen():
    print i

def gen2():
    for i in range(4):
        yield i

for i in gen2():
    print i

