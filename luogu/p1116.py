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
created by shhuan at 2020/7/15 22:24

"""


if __name__ == '__main__':
    # sys.stdin = open('p1116.in', 'r')
    N = int(input())
    A = []
    while len(A) < N:
        A += [int(x) for x in input().split()]

    ans = 0
    q = []
    for v in A:
        i = bisect.bisect_right(q, v)
        ans += len(q) - i
        q.insert(i, v)
    print(ans)