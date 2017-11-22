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
created by shhuan at 2017/11/21 20:40

"""

N = input()
A = [int(x) for x in input().split()]


c1 = A.count(1)
c2 = A.count(2)
c3 = A.count(3)
c4 = A.count(4)

c1 = max(0, c1-c3)

ans = c4+c3 + c2 // 2
c2 %= 2

if c2 == 1:
    c1 = max(c1-2, 0)
    ans += 1
ans += c1 // 4
if c1 % 4 != 0:
    ans += 1

print(ans)
