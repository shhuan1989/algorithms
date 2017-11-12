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
created by shhuan at 2017/11/8 22:47

"""


T = int(input())

for ti in range(T):
    N, P = map(int, input().split())

    if P <= 2:
        print('impossible')
    else:
        s = 'a' + 'b' * (P-2) + 'a'
        print(s * (N//P))