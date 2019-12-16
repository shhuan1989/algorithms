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
created by shhuan at 2019/12/10 23:28

"""

T = int(input())
for ti in range(T):
    N = int(input())
    scores = [0] * 12
    for i in range(N):
        p, s = map(int, input().split())
        scores[p] = max(scores[p], s)
    print(sum(scores[:9]))