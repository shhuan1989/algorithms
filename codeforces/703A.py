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
created by shhuan at 2017/11/22 21:04

"""

N = int(input())

a = 0
b = 0

for i in range(N):
    x, y = map(int, input().split())

    if x < y:
        b += 1
    if x > y:
        a += 1

if a == b:
    print("Friendship is magic!^^")
elif a > b:
    print("Mishka")
else:
    print("Chris")