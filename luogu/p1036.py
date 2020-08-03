# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

import itertools

if __name__ == '__main__':
    MAXN = 2 ** 20
    isprime = [True for _ in range(MAXN)]
    isprime[0] = False
    isprime[1] = False
    for i in range(2, MAXN):
        if isprime[i]:
            v = i + i
            while v < MAXN:
                isprime[v] = False
                v += i
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    
    ans = 0
    for vs in itertools.combinations(A, K):
        v = sum(vs)
        if isprime[v]:
            ans += 1
    print(ans)
    
    
    


