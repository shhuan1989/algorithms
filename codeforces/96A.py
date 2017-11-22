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
created by shhuan at 2017/11/21 20:34

"""

s = input()

if s.find("1111111") >= 0 or s.find("0000000") >= 0:
    print("YES")
else:
    print("NO")