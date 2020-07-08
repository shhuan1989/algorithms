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


def solve(N, K, A):
    
    M = 2 * K + 1
    x = [0 for _ in range(M)]
    
    add = [0 for _ in range(M)]
    minus = [0 for _ in range(M)]
    wc = collections.defaultdict(int)
    for i in range(N//2):
        a, b = A[i], A[N-i-1]
        wc[a+b] += 1
        s, t = min(a, b) + 1, max(a, b) + K + 1
        if s < M:
            add[s] += 1
        if t < M:
            minus[t] += 1
    
    s = 0
    for i in range(M):
        s += add[i]
        s -= minus[i]
        x[i] = s
        
    ans = N
    for target in range(2, M):
        one = x[target] - wc[target]
        two = N//2-wc[target]-one
        ans = min(ans, one + 2 * two)
        
    return ans
        
        
if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        N, K = map(int, input().split())
        A = [int(x) for x in input().split()]
        ans.append(solve(N, K, A))
    
    print('\n'.join(map(str, ans)))
    