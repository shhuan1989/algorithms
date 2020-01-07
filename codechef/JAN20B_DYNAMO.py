# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/4 11:50

"""

T = int(input())

for ti in range(T):
    N = int(input())
    A = int(input())
    S = A + 2 * 10**N
    print(S)
    sys.stdout.flush()
    B = int(input())
    S -= A + B
    C = S - 10**N
    print(C)
    sys.stdout.flush()
    D = int(input())
    print(S-D-C)
    sys.stdout.flush()
    ans = int(input())
    if ans == -1:
        exit(0)