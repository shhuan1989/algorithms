# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/11 18:30

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


def solve(s, p):
    wcs = collections.Counter(s)
    wcp = collections.Counter(p)
    for w, c in wcp.items():
        wcs[w] -= c

    ns = ''
    for ch in sorted(wcs.keys()):
        ns += ch * wcs[ch]

    ans = ns + p
    for i in range(len(ns)+1):
        t = ns[:i] + p + ns[i:]
        ans = min(ans, t)

    return ans


if __name__ == '__main__':
    T = int(input())
    for ti in range(T):
        s = input().strip()
        p = input().strip()
        print(solve(s, p))