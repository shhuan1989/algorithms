# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    
    a, b = 0, 1
    for i in range(1, N+1):
        a, b = a * i + b, b * i
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    a *= N
    c = gcd(a, b)
    a //= c
    b //= c
    
    d = a // b
    a %= b
    
    if a > 0:
        print(' '*len(str(d)) + str(a))
        print(str(d) + '-' * len(str(b)))
        print(' '*len(str(d)) + str(b))
    else:
        print(d)
    
    # print(a % b)
    
    