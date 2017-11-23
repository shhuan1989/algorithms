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
created by shhuan at 2017/11/23 10:59

"""



N = int(input())

O = [int(x) for x in input().split()]


if N == 2:
    print(abs(O[0]-O[1]), abs(O[0]-O[1]))
else:

    for i, v in enumerate(O):
        if i == 0:
            print(O[1]-O[0], O[-1]-O[i])
        elif i == N-1:
            print(O[-1]-O[0], O[-1]- O[-2])
        else:
            print(min(O[i+1]-O[i], O[i]-O[i-1]), max(O[i]-O[0], O[-1]-O[i]))