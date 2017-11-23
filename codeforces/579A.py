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
created by shhuan at 2017/11/22 21:21

"""



# a, a * 2**N <= x
# total = a + x-a*2**N


x = int(input())


ans = 0

while x > 0:
    if x % 2 == 1:
        ans += 1
    x //= 2

print(ans)











