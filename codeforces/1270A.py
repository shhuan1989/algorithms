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
created by shhuan at 2019/12/30 19:44

"""


T = int(input())
for ti in range(T):
    N, K1, K2 = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    print('YES' if max(A) > max(B) else 'NO')