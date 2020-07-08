# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import math


def is_pa(val):
    return val == val[::-1]


def to_dec(scale, val):
    return int(val, scale)


def to_scale(scale, val):
    if scale == 16:
        return hex(val)[2:]
    
    s = 0
    n = int(math.log(val, scale)) + 2
    for i in range(n, -1, -1):
        d = scale ** i
        s *= 10
        s += val // d
        val %= d
    
    return s
    

def add(scale, val):
    a = to_dec(scale, val)
    b = to_dec(scale, val[::-1])
    c = a + b
    d = to_scale(scale, c)
    return str(d)
    


def solve(scale, val):
    if is_pa(val):
        return 'STEP={}'.format(0)
    
    for step in range(1, 31):
        val = add(scale, val)
        if is_pa(val):
            return 'STEP={}'.format(step)
    
    return 'Impossible!'


if __name__ == '__main__':
    scale = int(input())
    v = input()
    print(solve(scale, v))
