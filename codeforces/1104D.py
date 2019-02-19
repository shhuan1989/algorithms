# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/15/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


while True:
    s = input()
    if s == 'end':
        exit(0)
    
    i = -1
    while True:
        print('? {} {}'.format(int(2**i), 2**(i+1)))
        s = input()
        if s == 'x':
            break
            
        i += 1
    
    l, r = int(2**i)+1, 2**(i+1)
    while l < r:
        m = (l+r) // 2
        print('? {} {}'.format(l, m))
        s = input()
        if s == 'x':
            r = m
        else:
            l = m + 1
    print('! {}'.format(l))