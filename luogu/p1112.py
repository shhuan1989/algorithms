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
created by shhuan at 2020/7/17 10:23

"""


if __name__ == '__main__':
    A, B, S, T, C = map(int, input().strip().split())
    wc = collections.defaultdict(int)
    for base in range(A, B+1):
        for a in range(1, base):
            for b in range(base):
                if a == b:
                    continue
                x = 0
                t = 0
                while x <= T:
                    if t % 2 == 0:
                        x = x * base + a
                    else:
                        x = x * base + b
                    t += 1
                    if S <= x <= T:
                        wc[x] += 1

    ans = [v for v in sorted(wc.keys()) if wc[v] == C]
    print('\n'.join(map(str, ans)))