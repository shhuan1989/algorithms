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
created by shhuan at 2020/7/19 15:12

"""



if __name__ == '__main__':
    A = [int(x) for x in input().strip().split()]
    N = A[0]
    A = A[1:]
    seen = set()
    for a, b in zip(A[:-1], A[1:]):
        seen.add(abs(a-b))

    if all([i in seen for i in range(1, N)]):
        print('Jolly')
    else:
        print('Not jolly')