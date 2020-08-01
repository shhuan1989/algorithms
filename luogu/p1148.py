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
created by shhuan at 2020/7/17 21:06

"""


def desc(v):
    if v == 0:
        return '0'
    elif v > 0:
        return '+{}'.format(v)
    else:
        return '{}'.format(v)

def solve(A):
    ans = [0, 0, 0, 0]
    if any([len(x) == 16 for x in A]) and len([x for x in A if not x]) == 3:
        for i in range(4):
            if len(A[i]) == 16:
                ans[i] = 1000
    else:
        hi = -1
        for i in range(4):
            if all(['H{}'.format(v) in A[i] for v in range(1, 14)]):
                hi = i
                break
        if hi >= 0:
            ans[hi] += 200
            if 'S12' in A[hi] and 'D11' in A[hi]:
                ans[hi] += 500
        H = [0, -50, -2, -3, -4, -5, -6, -7, -8, -9, -10, -20, -30, -40]
        for i in range(4):
            for v in A[i]:
                if hi < 0 and v.startswith('H'):
                    vi = int(v[1:])
                    ans[i] += H[vi]
            if 'S12' in A[i]:
                ans[i] += -100
            if 'D11' in A[i]:
                ans[i] += 100
        for i in range(4):
            if 'C10' in A[i]:
                if len(A[i]) == 1:
                    ans[i] = 50
                else:
                    ans[i] *= 2

    return ' '.join([desc(v) for v in ans])




if __name__ == '__main__':

    while True:
        A = []
        for i in range(4):
            line = input().strip().split()
            n = int(line[0])
            cards = line[1:]
            A.append(cards)
        if all([len(v) == 0 for v in A]):
            break

        print(solve(A))

