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
created by shhuan at 2017/11/22 22:18

"""

N = int(input())

A = [int(x) for x in input().split()]
ma = max(A)
ans = sum([ma-v for v in A])

print(ans)