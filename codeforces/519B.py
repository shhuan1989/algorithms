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
created by shhuan at 2017/11/22 20:56

"""

N = int(input())

A = collections.Counter([int(x) for x in input().split()])
B = collections.Counter([int(x) for x in input().split()])
C = collections.Counter(int(x) for x in input().split())

a = A-B
b = B-C

print(list(a.keys())[0])
print(list(b.keys())[0])