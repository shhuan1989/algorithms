# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def lis(A, equal):
    mx = max(A) + 1
    bits = [0 for _ in range(mx)]
    
    def update(index, val):
        while index < mx:
            bits[index] = max(bits[index], val)
            index |= index + 1
    
    def query(index):
        s = 0
        while index >= 0:
            if bits[index] > s:
                s = bits[index]
            index = (index & (index + 1)) - 1
        
        return s
    
    maxlen = 0
    for i, v in enumerate(A):
        c = query(v) if equal else query(v-1)
        c += 1
        maxlen = max(c, maxlen)
        # print(v, c+1)
        update(v, c)
    
    return maxlen
    

if __name__ == '__main__':
    A = [int(x) for x in input().split()]
    
    devices = lis(A, False)
    
    mx = max(A)
    A = [mx-v for v in A]
    
    maxshoot = lis(A, True)
    
    print(maxshoot)
    print(devices)
