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
created by shhuan at 2020/7/13 20:01

"""


if __name__ == '__main__':

    N = int(input())
    A = []
    for i in range(N):
        h, l, r = map(int, input().split())
        A.append((h, -i, l, r))
    A.sort()

    ansl = [0 for _ in range(N)]
    ansr = [0 for _ in range(N)]
    for i, (h, pos, l, r) in enumerate(A):
        pos = -pos
        for j in range(i-1, -1, -1):
            ph, ppos, pl, pr = A[j]
            ppos = -ppos
            if ph < h:
                if pl < l < pr and ansl[pos] == 0:
                    ansl[pos] = ppos + 1
                if pl < r < pr and ansr[pos] == 0:
                    ansr[pos] = ppos + 1
            if ansl[pos] > 0 and ansr[pos] > 0:
                break

    for i in range(N):
        print('{} {}'.format(ansl[i], ansr[i]))


