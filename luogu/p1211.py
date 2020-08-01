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
created by shhuan at 2020/7/25 14:41

"""


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]

    def mul(a, v):
        x = int(''.join(map(str, a))) * v
        return [int(x) for x in list(str(x))]


    def add(a, b):
        x = int(''.join(map(str, a)))
        y = int(''.join(map(str, b)))
        return [int(x) for x in list(str(x+y))]


    def getk(k, pre):
        if k <= 0:
            return [pre]

        x = []
        for v in A:
            x += getk(k-1, pre + [v])

        return x


    ans = 0
    for x in getk(3, []):
        for y in getk(2, []):
            if x[0] == 0 or y[0] == 0:
                continue
            a = mul(x, y[1])
            b = mul(x, y[0])
            if len(a) != 3 or len(b) != 3:
                continue
            if any([v not in A for v in a]) or any([v not in A for v in b]):
                continue

            c = add(a, b + [0])
            if len(c) == 4 and all([v in A for v in c]):
                ans += 1

    print(ans)