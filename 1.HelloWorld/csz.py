#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

def menu():
    print '[1].开始游戏    [2].退出游戏'

print '欢迎进入猜数字游戏'

flag = True
number = random.randint(0, 100)

try:
    while flag:
        i = int(raw_input('请输入数字：'))
        if i > number:
            print '大了'
        elif i < number:
            print '小了'
        else:
            print '恭喜你，答对了~'
            menu();
            j =  int(raw_input())
            if j > 1:
                flag = False

except Exception as e:
    sys.exit()
