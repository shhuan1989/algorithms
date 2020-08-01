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
created by shhuan at 2020/7/29 20:43

"""


if __name__ == '__main__':
    M = int(input())
    N = int(input())

    a = [int(x) for x in input().strip().split()]
    b = [int(x) for x in input().strip().split()]
    A = [(u, v) for u, v in zip(a, b)]
    A.sort()

    q = []
    for i, (u, v) in enumerate(A):
        heapq.heappush(q, v)
        while q and len(q) > u:
            M -= heapq.heappop(q)

    print(M)
