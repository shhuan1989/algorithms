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
created by shhuan at 2017/11/21 23:28

"""

N = int(input())


ans = N+1
while True:
    s = str(ans)
    if len(s) == len(set(s)):
        print(ans)
        exit(0)
    ans += 1