# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/3 20:43

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
    N = int(input())
    A = [int(x) for x in input().split()]
    avg = sum(A) // N
    S = [0 for _ in range(N)]
    for i, v in enumerate(A):
        S[i] = (S[i-1] if i > 0 else 0) + avg - A[i]

    S.sort()
    ans = sum([abs(S[N//2] - S[i]) for i in range(N)])
    print(ans)


