# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def solve(D, M):
    ans = 1
    for i in range(30):
        if D < (1 << i):
            break
        
        ans *= (min((1 << (i+1))-1, D) - (1 << i) + 2)
        ans %= M
        
    ans -= 1
    if ans < 0:
        ans += M
    
    return ans


if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        D, M = map(int, input().split())
        ans.append(solve(D, M))
    
    print('\n'.join(map(str, ans)))