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
created by shhuan at 2017/11/22 11:24

"""


# 1
# 1+2
# 1+2+3
# 1+2+3
# ...
# 1+2+3+..+h

# h(h+1)(h+2)/6

N = int(input())

ans = 1
for h in range(1, N):
    if h*(h+1)*(h+2) > N*6:
        ans = h-1
        break

print(ans)