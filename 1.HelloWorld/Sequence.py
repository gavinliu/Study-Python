#!/usr/bin/env python
# -*- coding: utf-8 -*-


s = [1,2,3,4,5,6,7,8]

print len(s)
print min(s)
print max(s)
print all(s)
print any(s)

print sum(s)

print s.count(5)
print s.index(5)

s.reverse()
print s
s.sort()
print s

s.append(9)
print s

l = [10,11]
s.extend(l)
print s

s.pop()
print s

del s[len(s) - 1]
print s
