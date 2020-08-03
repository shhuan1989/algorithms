# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

def check(v, k):
    p = []
    while v > 0:
        p.append(v % 10)
        v //= 10
    p = p[::-1]
    
    a = 100 * p[0] + 10 * p[1] + p[2]
    b = 100 * p[1] + 10 * p[2] + p[3]
    c = 100 * p[2] + 10 * p[3] + p[4]
    
    return all([v % k == 0 for v in [a, b, c]])


if __name__ == '__main__':
    K = int(input())
    
    ans = []
    for v in range(10000, 30001):
        if check(v, K):
            ans.append(v)
    
    if not ans:
        print('No')
    else:
        print('\n'.join(map(str, ans)))
    