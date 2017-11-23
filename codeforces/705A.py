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
created by shhuan at 2017/11/22 11:22

"""


N = int(input())

A = []

feels = ["hate", "love"]

for i in range(N):
    A.append(feels[i%2])


ans = "I " + " that I ".join(A) + " it"
print(ans)