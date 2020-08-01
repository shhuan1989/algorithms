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
created by shhuan at 2020/7/29 21:14

"""


def check(K, ops):
    A = [[0 for _ in range(2**K+1)] for _ in range(2**K+1)]

    for x, y, c in [[int(v) for v in op.split()] for op in ops]:
        A[x][y] = 1
        if c == 1:
            A[x][y-1] = 1
            A[x-1][y] = 1
        elif c == 2:
            A[x][y+1] = 1
            A[x-1][y] = 1
        elif c == 3:
            A[x][y-1] = 1
            A[x+1][y] = 1
        else:
            A[x+1][y] = 1
            A[x][y+1] = 1

    for row in A:
        print(' '.join(map(str, row)))




if __name__ == '__main__':
    K = int(input())
    x, y = map(int, input().strip().split())
    
    ans = []
    for r in range(1, x - 1 if x % 2 == 0 else x, 2):
        for c in range(1, 2 ** K + 1, 2):
            ans.append('{} {} {}'.format(2 * r, 2 * c - 1, 2))
            ans.append('{} {} {}'.format(2 * r - 1, 2 * c, 3))

    for c in range(1, y if y % 2 == 1 else y - 1, 2):
        ans.append('{} {} {}'.format(x if x % 2 == 0 else x + 1, 2 * c - 1, 2))
        ans.append('{} {} {}'.format(x - 1 if x % 2 == 0 else x, 2 * c, 3))
    if y % 2 == 0:
        if x % 2 == 0:
            ans.append('{} {} {}'.format(x - 1, y - 1, 4))
        else:
            ans.append('{} {} {}'.format(x + 1, y, 2))
    else:
        if x % 2 == 0:
            ans.append('{} {} {}'.format(x + 1, y - 1, 3))
        else:
            ans.append('{} {} {}'.format(x + 1, y + 1, 1))
    for c in range(y + 1 if y % 2 == 0 else y + 2, 2 ** K + 1, 2):
        ans.append('{} {} {}'.format(x if x % 2 == 0 else x + 1, 2 * c - 1, 2))
        ans.append('{} {} {}'.format(x - 1 if x % 2 == 0 else x, 2 * c, 3))

    for r in range(x + 1 if x % 2 == 0 else x + 2, 2 ** K + 1, 2):
        for c in range(1, 2 ** K + 1, 2):
            ans.append('{} {} {}'.format(2 * r, 2 * c - 1, 2))
            ans.append('{} {} {}'.format(2 * r - 1, 2 * c, 3))

    check(K, ans)
    # print('\n'.join(ans))