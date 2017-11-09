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
created by shhuan at 2017/11/8 08:41

"""

n, x = map(int, input().split())
A = [int(x) for x in input().split()]

if sum(A)+len(A)-1 == x:
    print('YES')
else:
    print('NO')