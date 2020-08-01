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
created by shhuan at 2020/7/19 17:10

"""


def solve(L, R, M):
    D = R-L
    for a in range(R, L-1, -1):
        k = (M+D) // a
        if k <= 0:
            continue

        v = k * a
        if M-D <= v <= M+D:
            diff = M-v
            b, c = L+abs(diff), L
            if diff < 0:
                b, c = c, b
            return '{} {} {}'.format(a, b, c)




if __name__ == '__main__':

    T = int(input())
    for ti in range(T):
        L, R, M = map(int, input().split())
        print(solve(L, R, M))