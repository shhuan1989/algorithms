# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2021/1/4

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


def check(K, H):
    heights = {0}
    
    for h in H:
        nh = set()
        for ph in heights:
            nh.add(ph + h)
        heights |= nh
    
    a = min([h for h in heights if h >= K])
    
    return sum(H) - a >= K
    

def solve(N, K, H):
    H.sort(reverse=True)
    
    if sum(H) < 2 * K:
        return -1
    
    total = H[0]
    for i in range(2, N+1):
        total += H[i-1]
        if total >= 2 * K and check(K, H[:i]):
            return i
    
    return -1
    # lo, hi = 2, N
    # while lo <= hi:
    #     mid = (lo + hi) // 2
    #     if check(K, H[:mid]):
    #         hi = mid - 1
    #     else:
    #         lo = mid + 1
    #
    # return lo if lo <= N else -1


if __name__ == '__main__':
    T = int(input())
    for ti in range(T):
        N, K = map(int, input().split())
        H = [int(x) for x in input().split()]
        print(solve(N, K, H))