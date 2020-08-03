# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/24

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def count(heights):
    # print(heights)
    s = 0
    for i in range(len(heights)):
        h = heights[i]
        for j in range(i, len(heights)):
            h = min(h, heights[j])
            s += h
    return s

# print(count([3, 2, 4]))

def solve(N, A):
    H = [0 for _ in range(N)]
    ans = 0
    for r, row in enumerate(A):
        for c, v in enumerate(row):
            if v == 0:
                H[c] = 0
            else:
                H[c] += 1
        
        l, r = 0, 0
        while r < N:
            if H[r] == 0:
                if l < r:
                    ans += count(H[l: r])
                l = r + 1
            r += 1
        if l < N:
            ans += count(H[l:])
    return ans
    

if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        row = [1 if v == 'W' else 0 for v in input().strip()]
        A.append(row)
    
    print(solve(N, A))