#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

html = urllib2.urlopen('http://www.baidu.com').read()

print html 
