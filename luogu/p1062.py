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
created by shhuan at 2020/7/10 18:25

"""




if __name__ == '__main__':
    K, N = map(int, input().split())
    M = 0
    while 2 ** M <= N:
        M += 1

    A = []

    def dfs(index, val):
        if index >= M:
            A.append(val)
            return

        dfs(index + 1, val + K**index)
        dfs(index + 1, val)

    dfs(0, 0)
    A.sort()
    print(A[N])