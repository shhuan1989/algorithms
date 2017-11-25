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
created by shhuan at 2017/11/24 17:57

"""

a, b = map(int, input().split())


ans = 0
while a > 0 and b > 0 and a + b > 2:
    if a < b:
        a += 1
        b -= 2
    else:
        b += 1
        a -=2
    ans += 1

print(ans)


