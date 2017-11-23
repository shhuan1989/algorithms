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
created by shhuan at 2017/11/22 21:33

"""

n, x = map(int, input().split())


if x == 1:
    print(1)

else:
    ans = 0
    for a in range(1, n+1):
        if x % a == 0 and x // a <= n:
            ans += 1

    print(ans)


