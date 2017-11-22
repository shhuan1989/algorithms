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
created by shhuan at 2017/11/21 20:10

"""

N, M, A = map(int, input().split())

r = N // A if N % A == 0 else N // A + 1
c = M // A if M % A == 0 else M // A + 1

print(r*c)