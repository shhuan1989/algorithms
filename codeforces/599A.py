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
created by shhuan at 2017/11/22 21:47

"""

d1, d2, d3 = map(int, input().split())


htoa = min(d1, d2+d3)
htob = min(d2, d1+d3)
atob = min(d3, d1+d2)

ans = htoa + atob + htob

print(ans)



