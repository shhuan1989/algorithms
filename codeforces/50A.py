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
created by shhuan at 2017/11/21 20:27

"""

N, M = map(int, input().split())

if N % 2 == 1 and M % 2 == 1:
    print((N*M - 1) // 2)
else:
    print(N*M // 2)