# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/8 21:40

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

from functools import lru_cache
if __name__ == '__main__':
    N, M, S = map(int, input().strip().split())
    W, V = [], []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)

    A = []
    for _ in range(M):
        l, r = map(int, input().split())
        A.append((l-1, r-1))

    presum = [0 for _ in range(N+1)]