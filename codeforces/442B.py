# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/16/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def cal(probs):
    np = [1-p for p in probs]
    
    p = 0
    left = 1
    right = 1
    for v in np:
        right *= v
        
    for i in range(len(probs)):
        right /= np[i]
        cp = left * right * probs[i]
        left *= np[i]
        p += cp
        
    return p
    

def solve(N, A):
    if any([abs(v-1.0) < 10**-9 for v in A]):
        print(1.0)
        return
        
    A.sort(reverse=True)
    ans = A[0]
    
    # if we choose x friends, we should choose those one has the bigger probability
    for size in range(2, N+1):
        if A[size - 1] == 0:
            break
        ans = max(ans, cal(A[:size]))
    
    print(ans)
    



N = int(input())
A = [float(x) for x in input().split()]
solve(N, A)