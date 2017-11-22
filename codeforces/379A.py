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
created by shhuan at 2017/11/22 00:59

"""


a, b = map(int, input().split())

ans = 0

c = 0
while a > 0:
    ans += a
    a, c = (a+c) // b, (a+c) % b


print(ans)