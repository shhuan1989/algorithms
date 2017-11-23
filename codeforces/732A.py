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
created by shhuan at 2017/11/22 11:47

"""

k, r = map(int, input().split())



# (k*ans) % 10 = ((k%10) * (ans%10)) % 10
k %= 10

ans = 1

while True:
    cost = k*ans
    if cost % 10 == 0 or cost % 10 == r:
        print(ans)
        exit(0)
    ans += 1