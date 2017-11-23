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
created by shhuan at 2017/11/22 13:00

"""


N = int(input())

# error N-1 times
# error N-2 times (N-2)*2
#...
# (N-1)+2(N-2)+...i(N-i) + ... + N-1


ans = 0
for i in range(1, N):
    ans += i * (N-i)
ans += N
print(ans)