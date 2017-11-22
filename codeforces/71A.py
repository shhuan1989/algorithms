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
created by shhuan at 2017/11/21 20:14

"""

N = int(input())

for i in range(N):
    w = input()
    if len(w) <= 10:
        print(w)
    else:
        print(w[0] + str(len(w)-2) + w[-1])