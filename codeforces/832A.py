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
created by shhuan at 2017/11/24 21:15

"""

N, K = map(int, input().split())

a = N // K
if a % 2 == 1:
    print("YES")
else:
    print("NO")