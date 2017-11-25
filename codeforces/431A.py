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
created by shhuan at 2017/11/24 14:26

"""

A = [0] + [int(x) for x in input().split()]

S = input()

ans = sum([A[int(i)] for i in list(S)])
print(ans)