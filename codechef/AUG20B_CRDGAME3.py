# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/11 21:01

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


def dfs(v, pre):
    if v < 10:
        return pre + 1

    return dfs(v-9, pre+1)


def bfs(v):
    if v == 0:
        return 1
    c = v // 9
    if v % 9 != 0:
        c += 1

    return c



if __name__ == '__main__':
    T = int(input())
    ans = []
    for t in range(T):
        C, R = map(int, input().strip().split())
        a, b = bfs(C), bfs(R)

        if a < b:
            ans.append((0, a))
        else:
            ans.append((1, b))

    print('\n'.join(['{} {}'.format(a, b) for a, b in ans]))
