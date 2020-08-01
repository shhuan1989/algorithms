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
created by shhuan at 2020/7/24 19:04

"""


MAXN = 2 * 10**5 + 5
bits = [0 for _ in range(MAXN)]

def update(index, val):
    while index < MAXN:
        bits[index] = max(bits[index], val)
        index |= index + 1


def query(index):
    s = 0
    while index >= 0:
        s = max(s, bits[index])
        index = (index & (index+1)) - 1

    return s



if __name__ == '__main__':
    N, D = map(int, input().split())
    index = MAXN-1

    ans = []
    for i in range(N):
        a, b = input().strip().split()
        b = int(b)
        if a == 'A':
            update(index, ((ans[-1] if ans else 0) + b) % D)
            index -= 1
        else:
            ans.append(query(index+b))

    print('\n'.join(map(str, ans)))



