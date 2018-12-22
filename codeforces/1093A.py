# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/15 22:35

"""


T = int(input())

for ti in range(T):
    x = int(input())

    ans = x // 7
    if x % 7 != 0:
        ans += 1
    print(ans)

