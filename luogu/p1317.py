# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/9 10:35

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
    B = []
    C = []
    for i, v in enumerate(A):
        if i == 0:
            B.append(v)
            C.append(1)
        else:
            if v == B[-1]:
                C[-1] += 1
            else:
                B.append(v)
                C.append(1)

    ans = 0
    for i in range(1, len(B)-1):
        if B[i] < B[i-1] and B[i] < B[i+1]:
            ans += 1
    # print(B)
    # print(C)
    print(ans)