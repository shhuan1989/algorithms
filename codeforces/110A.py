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
created by shhuan at 2017/11/21 23:10

"""

s = input()

c4 = s.count("4")
c7 = s.count("7")

def isLucky(x):
    x = str(x)
    a = x.count("4")
    b = x.count("7")

    return a + b == len(x)


if isLucky(c4+c7):
    print("YES")
else:
    print("NO")