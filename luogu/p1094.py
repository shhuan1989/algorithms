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
created by shhuan at 2020/7/11 17:05

"""


if __name__ == '__main__':
    W = int(input())
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))

    A.sort(reverse=True)
    ans = 0
    l, r = 0, N-1
    while l < r:
        if A[l] + A[r] > W:
            ans += 1
            l += 1
        else:
            ans += 1
            l += 1
            r -= 1
    if l == r:
        ans += 1

    print(ans)
