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
created by shhuan at 2017/11/22 12:52

"""

N, K = map(int, input().split())

A = [int(x) for x in input().split()]

A = [x for x in A if 5-x >= K]

print(len(A) // 3)