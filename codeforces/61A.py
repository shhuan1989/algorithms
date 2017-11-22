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
created by shhuan at 2017/11/22 00:35

"""

a = input()
b = input()

s = ""
for i in range(len(a)):
    u = a[i]
    v = b[i]
    if u != v:
        s += '1'
    else:
        s += '0'

print(s)