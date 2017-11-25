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
created by shhuan at 2017/11/23 22:41

"""


N = int(input())

A = [int(x) for x in input().split()]

odds = [x for x in A if x%2 == 1]
evens = [x for x in A if x%2 == 0]

ans = sum(evens or [0])

if odds:
    odds.sort()
    os = sum(odds)
    if os % 2 == 1:
        os -= odds[0]
    ans += os

print(ans)

