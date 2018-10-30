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
created by shhuan at 2018/10/19 22:49

"""


T = int(input())

for ti in range(T):
    s, a, b, c = map(int, input().split())
    bought = s // c
    total = bought + bought // a * b
    print(total)