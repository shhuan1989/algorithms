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
import math

def f(a, b, c, d, x):
    return a * x**3 + b * x**2 + c * x + d


def quadratic_root(a, b, c):
    d = math.sqrt(b**2-4*a*c)
    return (-b+d)/2/a, (-b-d)/2/a


def find(a, b, c, d, left, right):
    lo, hi = left, right
    while abs(lo-hi) > 1e-6:
        m = (lo + hi) / 2
        vl = f(a, b, c, d, lo)
        vm = f(a, b, c, d, m)
        if vl * vm > 0:
            lo = m
        else:
            hi = m
    
    return lo
        

if __name__ == '__main__':
    a, b, c, d = map(float, input().split())
    
    l, r = quadratic_root(3*a, 2*b, c)
    l, r = min(l, r), max(l, r)
    
    # print(l, r)
    
    x1 = find(a, b, c, d, -100, l)
    x2 = find(a, b, c, d, l, r)
    x3 = find(a, b, c, d, r, 100)
    print('{:.2f} {:.2f} {:.2f}'.format(x1, x2, x3))
