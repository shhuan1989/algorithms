# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/7/15 08:47

"""


def maxsun(a):
    presum = [0]
    for v in a:
        presum.append(presum[-1]+v)

    ans = float('-inf')
    minv = float('inf')
    for v in presum:
        ans = max(ans, v - minv)
        minv = min(minv, v)

    return ans

if __name__ == '__main__':
    # sys.stdin = open('p1121.in', 'r')
    N = int(input())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().split()]
    A += A

    presum = [0]
    for v in A:
        presum.append(presum[-1] + v)

    maxsum = float('-inf')
    maxl, maxr = -1, -1
    q = collections.deque()
    for i, v in enumerate(presum):
        while q and i-q[0][1] > N:
            q.popleft()
        if q:
            s = v - q[0][0]
            if s > maxsum or (s == maxsum and i-q[0][1] < maxr-maxl):
                maxsum = s
                maxl = q[0][1]
                maxr = i
        while q and q[-1][0] >= v:
            q.pop()
        q.append((v, i))

    ansa = maxsum
    ansb = maxsum
    addedRight = False
    if maxr - maxl < N:
        right = A[maxr: maxl+N]
        rightmax = maxsun(right)
        ansa += rightmax
    # split [maxl, maxr] into 2 segments
    if maxr - maxl > 1:
        seg = [-v for v in A[maxl: maxr]]
        ansb += maxsun(seg)
    else:
        ansb = float('-inf')

    ans = max(ansa, ansb)
    print(ans)


