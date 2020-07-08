# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


# c = a ^ b
# a < b < c


def solve(N):
    if N == 0:
        return 0
    
    right = 0
    have = 0
    while True:
        r2 = 2 ** right
        if have + r2 * (2 + r2) > N:
            break
        
        have += r2 * (2 + r2)
        right += 2
    
    rest = N - have
    
    # 01xxx
    # 10xxx
    # 11xxx
    right += 2
    
    
    r2 = 2 ** right
    r3 = r2 * (2 + r2)
    if rest % r3 == 0:
        a = 2 * r2
        a += rest // r2
        return a
    
    a = rest // r2
    b = rest % r2
    
    
    
    
    
    
    
    
    
    



if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        N = int(input())
        ans.append(solve(N))
    
    print('\n'.join(map(str, ans)))