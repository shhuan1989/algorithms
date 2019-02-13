# -*- coding: utf-8 -*-
"""
created by shhuan at 2018/10/20 22:37

"""


import collections
import heapq

import bisect






def f1n(n):
    ans = 1
    d = 1
    for i in range(1, n+1):
        d /= i
        ans += d
    
    return ans


def f2n(n):
    return pow(1+1/n, n)

for n in range(100000, 100010):
    print(f1n(n), f2n(n))