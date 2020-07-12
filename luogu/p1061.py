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
created by shhuan at 2020/7/10 18:32

"""


A = [chr(ord('a')+i) for i in range(26)]


def dfs(s, t, i, l, r, increased):
    if i >= len(s):
        return [[v for v in t]]

    ans = []
    for v in range((s[i] if not increased else t[i-1])+1, r+1):
        t[i] = v
        ans += dfs(s, t, i+1, l, r, True)

    return ans


def solve(s, l, r):

    ans = []
    for i in range(len(s)-1, -1, -1):
        t = s.copy()
        ans += dfs(s, t, i, l, r, False)
        if len(ans) >= 5:
            break

    return [''.join([A[i] for i in v]) for v in ans]


if __name__ == '__main__':
    S, T, W = map(int, input().split())
    N = T - S + 1
    S -= 1
    T -= 1
    val = list([ord(v)-ord('a') for v in input().strip()])

    print('\n'.join(solve(val, S, T)[:5]))

