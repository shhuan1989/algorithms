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
created by shhuan at 2017/11/24 13:57

"""

n, a, b = map(int, input().split())

ans = (a + b - 1 + n * abs(b)) % n + 1
print(ans)


