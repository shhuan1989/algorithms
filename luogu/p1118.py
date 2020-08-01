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
created by shhuan at 2020/7/15 21:48

"""

A = [[0], [1], [1, 1]]
for i in range(2, 13):
    p = A[-1]
    a = [1] + [p[i]+p[i+1] for i in range(len(p)-1)] +[1]
    A.append(a)


def check(N, S, P):
    return sum([a*b for a, b in zip(P, A[N])]) == S

USED = [False for _ in range(15)]

def dfs(N, P, S, index, val):
    if index >= N:
        if val == S:
            print(' '.join(map(str, P)))
            exit(0)
        return

    if val > S:
        return

    for i in range(1, N+1):
        if not USED[i]:
            USED[i] = True
            P[index] = i
            dfs(N, P, S, index + 1, val + P[index] * A[N][index])
            USED[i] = False

# print(sum([(a*b) for a, b in zip([1, 2, 3, 4], A[4])]))
if __name__ == '__main__':
    N, S = map(int, input().split())
    dfs(N, [i for i in range(1, N+1)], S, 0, 0)