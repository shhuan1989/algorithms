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
created by shhuan at 2017/11/24 17:02

"""

# a, b
# a-b, b
# ... => b, a-kb
#

def cal(a, b):
    if a < b:
        return cal(b, a)

    if a == b:
        return 1
    if a == 0 or b == 0:
        return 0

    k = a//b

    return k + cal(b, a-k*b)

a, b = map(int, input().split())


print(cal(a, b))