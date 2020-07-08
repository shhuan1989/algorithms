# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/30

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def check(have,  m, k):
    if k % m == 0:
        return True
    
    k %= m
    
    cycle = [-1 for i in range(m)]
    for i in range(m):
        if cycle[i] < 0:
            a, b = i, (i+k) % m
            size = 0
            while cycle[a] < 0:
                size += 1
                cycle[a] = b
                a, b = b, (b+k) % m
            
            ti, diff = -1, 5000
            for hi, hv in enumerate(have):
                d = hv - size
                if 0 <= d < diff:
                    diff = d
                    ti = hi
                    
            if ti < 0:
                return False
            
            have[ti] -= size
    
    return True
    
    


def solve(N, K, S):
    wc = collections.Counter(S)
    have = list(wc.values())
    have.sort(reverse=True)
    ans = 0
    for p in range(1, K+1):
        if K % p != 0:
            continue
        if p > K:
            break
        for m in range(N, ans, -1):
            if check(have.copy(), m, p):
                ans = max(ans, m)
                break

    return ans


if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        N, K = map(int, input().split())
        S = list(input())
        ans.append(solve(N, K, S))
    
    print('\n'.join(map(str, ans)))