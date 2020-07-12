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
created by shhuan at 2020/7/9 21:35

"""




if __name__ == '__main__':
    N, M, K, L, D = map(int, input().split())
    A = []
    B = []
    for i in range(D):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == x2:
            A.append(min(y1, y2))
        else:
            B.append(min(x1, x2))

    wca = collections.Counter(A)
    wca = [(c, y) for y, c in wca.items()]
    wcb = collections.Counter(B)
    wcb = [(c, x) for x, c in wcb.items()]
    wca.sort(reverse=True)
    wcb.sort(reverse=True)

    print(' '.join(map(str, sorted([x for c, x in wcb[:K]]))))
    print(' '.join(map(str, sorted([y for c, y in wca[:L]]))))
