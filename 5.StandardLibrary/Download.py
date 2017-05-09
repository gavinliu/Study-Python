#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2


url = 'http://img.xiami.net/images/album/img25/58825/3309101383205489.jpg'


name = 'LaLa首张创作专辑'
artist = '徐佳莹'
formate = url[url.rindex('.'):]

dirPath = 'cover/' + artist
filePath = 'cover/' + artist + '/' + name + formate

if os.path.exists(filePath):
    print '11'
    pass
else:
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

    f = urllib2.urlopen(url)
    with open(filePath, "wb") as code:
        code.write(f.read()) 