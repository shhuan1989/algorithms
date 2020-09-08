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
    a, b = map(int, input().split())
    
    def exgcd(a, b):
        if b:
            x, y, d = exgcd(b, a % b)
            return y, x-a//b*y, d
        else:
            return 1, 0, a
        
    x, y, d = exgcd(a, b)
    
    x *= -1
    a *= -1
    
    while x < 0 or y < 0:
        x += b // d if x < 0 else 0
        y -= a // d if x >= 0 else 0
        
    print(d)
    print(x, y)