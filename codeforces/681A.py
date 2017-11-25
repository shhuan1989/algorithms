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
created by shhuan at 2017/11/24 22:31

"""

N = int(input())


for i in range(N):
    a, b, c = input().split()
    b, c = int(b), int(c)

    if b >= 2400 and c > b:
        print("YES")
        exit(0)

print("NO")