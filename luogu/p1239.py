# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
from functools import lru_cache


@lru_cache(maxsize=None)
def ncr(c, r):
    if c < r:
        return 0
    
    if r == 0 or r == c:
        return 1
    
    if c-r < r:
        return ncr(c, c-r)
    
    return ncr(c-1, r-1) + ncr(c-1, r)


def brutal(K):
    wc = collections.defaultdict(int)
    
    for v in range(1, K+1):
        while v > 0:
            wc[v % 10] += 1
            v //= 10
        
    return [wc[i] for i in range(10)]


def solve(K):
    K = [int(x) for x in list(str(K))]
    N = len(K)
    
    # op == 0 equal
    # op == -1 less
    # op == 1 greater
    wc = collections.defaultdict(int)
    
    def dfs(index, st, op):
        if index >= N:
            if op <= 0:
                while st > 0:
                    wc[st % 10] += 1
                    st //= 10
            
            return
        
        if op == 0:
            for i in range(K[index]):
                dfs(index + 1, st * 10 + i, -1)
            dfs(index + 1, st * 10 + K[index], 0)
        elif op < 0:
            rest = N - index
            count = 0
            for i in range(1, rest + 1):
                count += i * ncr(rest, i) * 9 ** (rest - i)
            for i in range(1, 10):
                wc[i] += count
            
            v = st
            while v > 0:
                wc[v % 10] += 10**rest
                v //= 10
            
            if st > 0:
                wc[0] += count
            else:
                # first non-zero at i
                for i in range(index, N):
                    rest = N-i-1
                    for i in range(1, rest+1):
                        wc[0] += i * ncr(rest, i) * 9 **(rest-i+1)
                
    
    # print(K)
    for i in range(K[0]):
        dfs(1, i, -1)
    dfs(1, K[0], 0)
    
    return [wc[i] for i in range(10)]

if __name__ == '__main__':
    K = int(input())
    
    # for i in range(10000):
    #     if brutal(i) != solve(i):
    #         print(i)
    #         exit(0)
    
    print('\n'.join(map(str, solve(K))))
    # print(solve(K))
    # print(brutal(K))