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
created by shhuan at 2020/7/8 22:34

"""


def gcd(x, y):
    while y:
        x, y = y, x%y

    return x


def solve(x, y):
    if y % x != 0:
        return 0

    y //= x
    if y == 1:
        return 1

    ans = 0
    for k in range(1, int(math.sqrt(y))+2):
        if y % k == 0:
            m = y // k
            if gcd(k, m) > 1:
                continue
            if m < k:
                break
            ans += 2

    return ans

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(solve(x, y))