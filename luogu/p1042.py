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
created by shhuan at 2020/7/9 19:50

"""


def solve(s, score):
    pa = []
    a, b = 0, 0
    for i, v in enumerate(s):
        if v == 'E':
            break
        if v == 'W':
            a += 1
        elif v == 'L':
            b += 1

        if max(a, b) >= score and abs(a - b) >= 2:
            pa.append('{}:{}'.format(a, b))
            a = 0
            b = 0
    if a > 0 or b > 0:
        pa.append('{}:{}'.format(a, b))
    else:
        pa.append('{}:{}'.format(a, b))

    return '\n'.join(pa)


if __name__ == '__main__':
    S = ''
    for line in sys.stdin:
        S += line

    a = solve(S, 11)
    b = solve(S, 21)
    print(a)
    print()
    print(b)