# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/8 10:18

"""

N = int(input())

S = input()

B = [int(x) for x in input().split()]


WC = collections.Counter(S)


def dfs(s, wc, n):
    if len(s) == n:
        b = sum([B[i] for i in range(n) if s[i] == S[i]] or [0])
        return b

    ans = float('-inf')
    ws = [k for k in wc.keys() if wc[k] > 0]
    for a in ws:
        for b in ws:
            if a != b:
                wc[a] -= 1
                wc[b] -= 1
                ans = max(ans, dfs(a+s+b, wc, n))
                wc[a] += 1
                wc[b] += 1

    return ans

print(dfs("", WC, N))