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
from functools import cmp_to_key

"""
created by shhuan at 2020/8/1 11:46

"""



if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().strip().split()]
    B = [int(x) for x in input().strip().split()]
    jobs = [(a, b, i, 0) for i, (a, b) in enumerate(zip(A, B))]

    p = [v for v in jobs if v[0] < v[1]]
    q = [v for v in jobs if v[0] >= v[1]]
    p.sort(key=cmp_to_key(lambda a, b: a[0] - b[0]))
    q.sort(key=cmp_to_key(lambda a, b: b[1] - a[1]))
    p += q
    t1, t2 = 0, 0
    for job in p:
        t1 += job[0]
        t2 = max(t2, t1) + job[1]

    print(t2)
    print(' '.join(map(str, [v[2]+1 for v in p])))
