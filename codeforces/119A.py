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
created by shhuan at 2017/11/22 01:50

"""

a, b, n = map(int, input().split())


def gcd(x,y):
    if x < y:
        return gcd(y, x)

    if y == 0:
        return x

    return gcd(y, x%y)


simon = True
while n > 0:
    if simon:
        simon = False
        n -= gcd(a, n)
    else:
        simon = True
        n -= gcd(b, n)

if simon:
    print(1)
else:
    print(0)