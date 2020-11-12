# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/6

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('P1414_12.in', 'r')
    N = int(input())
    A = [int(x) for x in input().split()]
    
    maxv = 10**3+10
    isprime = [True for _ in range(maxv+1)]
    for i in range(2, maxv+1):
        if isprime[i]:
            v = i + i
            while v <= maxv:
                isprime[v] = False
                v += i
    primes = [i for i in range(2, maxv+1) if isprime[i]]
    
    
    def defact(x):
        ret = []
        for v in primes:
            if v > x:
                break
            if x % v == 0:
                # ret.append(v)
                c = 0
                while x % v == 0:
                    c += 1
                    x //= v
                ret.append((v, c))
                
        if x > 1:
            ret.append((x, 1))
        return ret
    
    
    maxa = max(A)
    count = [0 for _ in range(maxa+1)]


    def dfs(index, parts, pre):
        if index >= len(parts):
            count[pre] += 1
            return
        for i in range(parts[index][1] + 1):
            dfs(index + 1, parts, pre * parts[index][0] ** i)
        
    def countdivisor(x):
        parts = defact(x)
        dfs(0, parts, 1)
    
    
    for x in A:
        countdivisor(x)
    
    # print(count)
    ans = []
    y = maxa
    for k in range(1, N+1):
        while count[y] < k:
            y -= 1
        ans.append(y)
    
    print('\n'.join(map(str, ans)))
            
        