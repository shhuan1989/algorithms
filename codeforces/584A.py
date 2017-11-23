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
created by shhuan at 2017/11/22 11:44

"""

n, t = map(int, input().split())


ans = 10**n - 1

ans //= t

ans *= t

if ans > 0 and len(str(ans)) == n:
    print(ans)
else:
    print(-1)