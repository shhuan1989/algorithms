# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/11 21:19

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
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        P = [int(x) for x in input().split()]

        step = float('inf')
        p = -1
        for pos in P:
            if pos > K:
                continue
            if K % pos == 0:
                s = K // pos
                if s < step:
                    step = s
                    p = pos
        print(p)