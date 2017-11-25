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
created by shhuan at 2017/11/24 20:33

"""


n, m = map(int, input().split())

# x: 1, 2
# y: 2, 1
# x+2y <= n; 2x+y <=m
# 2x+4y <= 2n
# 3y <= 2n-m
# 3x <= 2m-n

# maximize x+y

# 3(x+y) <= 2n-m+2m-n = m+n
# x+y <= (m+n)//3
#

ans = 0
for x in range(min(n, (n+m)//3)+1):
    y = min((n-x)//2, m-2*x)
    if y >= 0:
        ans = max(ans, x+y)

print(ans)




