# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/9 10:19

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


if __name__ == '__main__':
    # sys.stdin = open('P1318_6.in', 'r')
    N = int(input())
    A = [int(x) for x in input().split()][:N]
    # N = len(A)
    left, right = [0 for _ in range(N)], [0 for _ in range(N)]

    for i, v in enumerate(A):
        left[i] = max(left[i-1] if i > 0 else 0, v)

    for i in range(N-1, -1, -1):
        right[i] = max(right[i+1] if i+1 < N else 0, A[i])

    ans = 0
    for i, v in enumerate(A):
        ans += max(0, min(left[i], right[i]) - v)

    print(ans)