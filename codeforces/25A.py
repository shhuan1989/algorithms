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
created by shhuan at 2017/11/22 01:32

"""

N = int(input())

A = [int(x) for x in input().split()]

odds = [x for x in A if x%2 == 1]
evens = [x for x in A if x%2==0]

if len(odds) == 1:
    print(A.index(odds[0])+1)
else:
    print(A.index(evens[0])+1)