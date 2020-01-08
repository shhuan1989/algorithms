# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/30/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

N, M = map(int, input().split())
A = [int(x) for x in input().split()]


def solve(N, M, A):
    if M in A:
        return 'YES'
    
    A = [v % M for v in A]
    wc = collections.Counter(A)
    
    seen = set()
    for w, c in wc.items():
        x = set()
        c = min(M+1, c)
        for v in seen | {0}:
            x |= {(v+w*i) % M for i in range(1, c+1)}
        
        seen |= x
        if 0 in seen:
            return 'YES'
    
    return 'NO'
        
    
print(solve(N, M, A))




