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
created by shhuan at 2020/7/25 20:07

"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        p, a = map(int, input().split())
        A.append((p, a))

    A.sort()
    ans = 0
    ai = 0
    while N > 0 and ai < M:
        p, a = A[ai]
        if N <= a:
            ans += p * N
            break
        else:
            ans += p * a
            N -= a
        ai += 1
    print(ans)

