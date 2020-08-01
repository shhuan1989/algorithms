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
created by shhuan at 2020/7/20 21:07

"""

if __name__ == '__main__':
    N = int(input())
    wc = collections.defaultdict(int)
    for i in range(N):
        a, t = input().split()
        a = float(a)
        t = int(t)

        for k in range(1, t+1):
            w = int(math.floor(k * a))
            wc[w] += 1

    for w in sorted(wc.keys()):
        if wc[w] % 2 !=  0:
            print(w)
            exit(0)