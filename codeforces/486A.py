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
created by shhuan at 2017/11/22 00:01

"""


# f = -1-3-5-... + 2 + 4 + ..
# a = 1+3+5+..2*n-1 = (2n-1+1)n/2 = n**2
# b = 2+4 + 6+.. + 2*n = (2+2n)n//2 = n(n+1)

N = int(input())
na = (N+1)//2
nb = N//2

a = na**2
b = nb*(nb+1)

print(b-a)


