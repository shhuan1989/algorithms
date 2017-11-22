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
created by shhuan at 2017/11/22 00:26

"""

N, K = map(int, input().split())

# 1, 3, 5, ... 2*n-1
# count of odd numbers is n

nodd = (N+1)//2
neven = N//2

if nodd >= K:
    print(2*K-1)
else:
    K -= nodd
    print(2*K)

