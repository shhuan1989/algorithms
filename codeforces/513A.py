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
created by shhuan at 2017/11/22 22:59

"""

n1, n2, k1, k2 = map(int, input().split())

if n1 <= n2:
    print("Second")
else:
    print("First")