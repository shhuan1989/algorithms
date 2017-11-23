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
created by shhuan at 2017/11/22 10:12

"""

N = int(input())

S = input()

a = S.count("A")
d = S.count("D")

if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")