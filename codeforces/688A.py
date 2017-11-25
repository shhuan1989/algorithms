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
created by shhuan at 2017/11/24 19:50

"""

N, D = map(int, input().split())

ans = 0
p = 0
for i in range(D):
    s = input()
    if all(x=='1' for x in s):
        ans = max(ans, i-p)
        p = i+1
ans = max(ans, D-p)
print(ans)
