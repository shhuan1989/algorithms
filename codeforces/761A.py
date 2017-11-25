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
created by shhuan at 2017/11/24 19:28

"""

a, b = map(int, input().split())


if a+b > 0 and abs(a-b) <= 1:
    print("YES")
else:
    print("NO")