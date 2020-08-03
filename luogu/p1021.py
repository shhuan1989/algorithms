# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



COINS = [0 for _ in range(20)]
N, K = 0, 0
MAXN = 50000


def getMax(coinCount):
    needs = [i for i in range(MAXN)]
    for ci in range(1, coinCount):
        c = COINS[ci]
        # for i in range(MAXN):
        #     for j in range(1, (MAXN-i) // c):
        #         k = i + j * c
        #         needs[k] = min(needs[k], needs[i] + j)
        for i in range(c, c*N+1):
            needs[i] = min(needs[i], needs[i-c]+1)
    
    for i in range(MAXN):
        if needs[i] > N:
            return i-1
    
    return MAXN


def dfs(coinCount, maxVal):
    if coinCount == K:
        return maxVal, [COINS[i] for i in range(coinCount)]

    ansv, ansc = 0, []
    for newCoin in range(COINS[coinCount-1]+1, max(COINS[coinCount-1]+5, maxVal)+1):
        COINS[coinCount] = newCoin
        v, c = dfs(coinCount+1, getMax(coinCount+1))
        if v > ansv:
            ansv = v
            ansc = c
    
    return ansv, ansc
        

def solve():
    COINS[0] = 1
    v, c = dfs(1, 0)
    print(' '.join(map(str, c)))
    print('MAX={}'.format(v))


if __name__ == '__main__':
    N, K = map(int, input().split())
    solve()