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
created by shhuan at 2017/11/21 23:35

"""

s = input()
t = input()

if s == t[::-1]:
    print("YES")
else:
    print("NO")