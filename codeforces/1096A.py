# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/28 22:38

"""

T = int(input())

ans = []
for ti in range(T):
    l, r = map(int, input().split())

    ans.append((l, 2*l))


print('\n'.join(['{} {}'.format(x, y) for x, y in ans]))
