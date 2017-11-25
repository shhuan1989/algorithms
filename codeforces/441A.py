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
created by shhuan at 2017/11/24 20:29

"""


N, K = map(int, input().split())

ans = []
for i in range(N):
    a = [int(x) for x in input().split()]

    if any(K > v for v in a[1:]):
        ans.append(i+1)

print(len(ans))
if ans:
    print(" ".join(map(str, ans)))