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
created by shhuan at 2017/11/21 20:16

"""

N, K = map(int, input().split())
A = [int(x) for x in input().split()]

t = A[K-1]

print(len([v for v in A if v >= t and v > 0]))