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
created by shhuan at 2017/11/24 18:35

"""

n, k, l, c, d, p, nl, np = map(int, input().split())

ans = 0

print(min(l*k//nl, c*d, p//np)//n)