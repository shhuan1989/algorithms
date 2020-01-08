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

N, T = map(int, input().split())
A = [int(x) for x in input().split()]
magic = 1000
MAXV = 10**6+5
Q = []
for i in range(T):
    l, r = map(int, input().split())
    Q.append((l//magic, l-1, r, i))


count = [0 for _ in range(MAXV)]
ans = [0 for _ in range(T)]
curAns = [0]


def remove(val):
    curAns[0] -= count[val] ** 2 * val
    count[val] -= 1
    curAns[0] += count[val] ** 2 * val


def add(val):
    curAns[0] -= count[val] ** 2 * val
    count[val] += 1
    curAns[0] += count[val] ** 2 * val


def solve():
    Q.sort()
    left, right = 0, 0
    for d, l, r, i in Q:
        while left < l:
            remove(A[left])
            left += 1
        while left > r:
            left -= 1
            add(A[left])
        while right < r:
            add(A[right])
            right += 1
        while right > r:
            right -= 1
            remove(A[right])
        ans[i] = curAns[0]
    
    
solve()
print('\n'.join(map(str, ans)))
