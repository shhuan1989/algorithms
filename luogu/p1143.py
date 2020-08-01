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
created by shhuan at 2020/7/17 22:57

"""


CH = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']


def to_ndim(val, base):
    ans = []
    while val > 0:
        ans += CH[val % base]
        val //= base

    return ''.join(ans[::-1])


def ch2val(ch):
    if ord('0') <= ord(ch) <= ord('9'):
        return int(ch)

    return ord(ch)-ord('A')+10


def to_dec(val, base):
    ans = 0
    p = 1
    for i in range(len(val)-1, -1, -1):
        ans += ch2val(val[i]) * p
        p *= base

    return ans


if __name__ == '__main__':
    A = int(input())
    S = input().strip()
    B = int(input())

    print(to_ndim(to_dec(S, A), B))