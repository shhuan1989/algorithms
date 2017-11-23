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
created by shhuan at 2017/11/22 20:32

"""

N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(input())

for row in A:
    if "C" in row or "M" in row or "Y" in row:
        print("#Color")
        exit(0)

print("#Black&White")