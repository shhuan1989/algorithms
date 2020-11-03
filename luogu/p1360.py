# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('P1360_2.in', 'r')
    N, M = map(int, input().split())
    
    state = [0] * M
    
    def myhash():
        return '-'.join(map(str, state))
    
    minindex = {myhash():-1}
    ans = 0
    for ci in range(N):
        v = int(input())
        
        for i in range(M):
            if v & (1 << i):
                state[i] += 1
        
        x = min(state)
        for i in range(M):
            state[i] -= x
        
        h = myhash()
        if h in minindex:
            ans = max(ans, ci - minindex[h])
        else:
            minindex[h] = ci
    
    
    print(ans)
    