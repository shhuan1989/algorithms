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
created by shhuan at 2017/11/22 22:40

"""

a, b = map(int, input().split())


# a*3**N >= b*2**N

ans = 1
while a * (3**ans) <= b * (2**ans):
    ans += 1

print(ans)