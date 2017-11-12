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
created by shhuan at 2017/11/8 22:03

"""

T = int(input())


for ti in range(T):
    S = input()

    l = -1
    a = 0
    b = 0
    for i, v in enumerate(S):
        if v != '.':
            if l >= 0 and S[l] == v:
                if v == 'A':
                    a += i - l - 1
                else:
                    b += i - l - 1
            l = i
            if v == 'A':
                a += 1
            else:
                b += 1
    print(a, b)

