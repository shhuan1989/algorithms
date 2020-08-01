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
import random

"""
created by shhuan at 2020/7/20 19:35

"""


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().strip().split()]
    # N = 10**5
    # A = [random.randint(0, 10**9) for _ in range(N)]
    q1, q2 = [], []
    ans = []
    for i, v in enumerate(A):
        if not q2:
            heapq.heappush(q2, v)
        else:
            if v > q2[0]:
                heapq.heappush(q2, v)
            else:
                heapq.heappush(q1, -v)

        while len(q1) > len(q2):
            a = heapq.heappop(q1)
            heapq.heappush(q2, -a)
        while len(q2) - len(q1) > 1:
            a = heapq.heappop(q2)
            heapq.heappush(q1, -a)
        if i % 2 == 0:
            ans.append(q2[0])

    print('\n'.join(map(str, ans)))