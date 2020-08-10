# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/1 12:30

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List



if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().strip().split()]

    s = A[0]
    for v in A[1:]:
        s ^= v

    if s == 0:
        print('lose')
    else:
        for i, v in enumerate(A):
            if s ^ v <= v:
                print('{} {}'.format(v - (s^v), i+1))
                A[i] = s ^ v
                print(' '.join(map(str, A)))
                exit(0)

