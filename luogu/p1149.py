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
created by shhuan at 2020/7/17 20:33

"""


STICKS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def cost(v):
    if v == 0:
        return STICKS[0]
    c = 0
    while v > 0:
        c += STICKS[v % 10]
        v //= 10

    return c

def dfs(a, b, rest, ina):
    if rest <= 0:
        return 0

    ans = 0
    cc = cost(a+b)
    if rest == cc:
        # if b > 0:
            # print(a, b, a+b)
        ans += 1 if b > 0 else 0


    if ina:
        for v in range(10) if a > 0 else range(1, 10):
            ans += dfs(a*10+v, b, rest-cost(v), True)
            ans += dfs(a * 10 + v, b, rest - cost(v), False)
    else:
        for v in range(10) if b > 0 else range(1, 10):
            ans += dfs(a, b*10+v, rest-cost(v), False)

    return ans


def dfs2(rest, first, pre):
    if rest < pre:
        return 0

    if rest == pre:
        return 1 if not first else 0

    ans = 0
    if first:
        for i in range(1, 10):
            ans += dfs2(rest-cost(i), False, pre+cost(i))
    else:
        for i in range(10):
            ans += dfs2(rest-cost(i), False, pre+cost(i))
    return ans



if __name__ == '__main__':
    N = int(input())
    N -= 4
    ans = dfs(0, 0, N, True)

    # 0 + 0 = 0
    if N == 18:
        ans += 1
    # x + 0 = x, 0 + x = x
    ans += dfs2(N-6, True, 0) * 2


    print(ans)

