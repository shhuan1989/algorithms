# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/9 04:05

"""

T = int(input())
for ti in range(T):
    N = int(input())
    cnt = [0] * 10
    for _ in range(N):
        line = input()
        for i, v in enumerate(line):
            if v == '1':
                cnt[i] += 1

    ans = sum([v % 2 for v in cnt])
    print(ans)

