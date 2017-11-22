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
created by shhuan at 2017/11/22 01:48

"""

a = input()
b = input()
c = input()

wca = collections.Counter(a)
wcb = collections.Counter(b)
wcc = collections.Counter(c)

if wca + wcb == wcc:
    print("YES")
else:
    print("NO")