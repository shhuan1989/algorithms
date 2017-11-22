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
created by shhuan at 2017/11/21 20:33

"""

N = int(input())
ans = 0

for i in range(N):
    s = input()
    if s.find('++') >= 0:
        ans += 1
    else:
        ans -= 1

print(ans)