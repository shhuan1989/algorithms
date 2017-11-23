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
created by shhuan at 2017/11/22 22:32

"""


N, M = map(int, input().split())


minStep = N//2 if N%2 == 0 else N//2+1
for step in range(minStep, N+1):
    if step % M == 0:
        print(step)
        exit(0)
print(-1)