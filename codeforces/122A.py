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
created by shhuan at 2017/11/21 22:49

"""

N = int(input())


for i in range(1, N//2+1):
    if N % i == 0:
        for si in [str(i), str(N//i)]:
            c4 = si.count('4')
            c7 = si.count('7')
            if c4 + c7 == len(si):
                print("YES")
                exit(0)

print("NO")