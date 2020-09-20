# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/9 11:15

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
    A = [int(x) for x in input().split()]
    N = A[0]
    ans = []

    zero = True
    for v in A[1:]:
        if zero:
            ans += [0] * v
        else:
            ans += [1] * v
        zero = not zero

    for i in range(0, N*N, N):
        print(''.join(map(str, ans[i: i+N])))