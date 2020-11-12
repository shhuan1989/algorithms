# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/20 18:49

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

    def solve(A, N):
        # 00, 11
        a = [(0, 1), (1, 0)]
        b = [(N-1, N-2), (N-2, N-1)]

        for x, y in [(0, 1), (1, 0)]:
            invert = 0
            for r, c in a:
                if A[r][c] != x:
                    invert += 1
            for r, c in b:
                if A[r][c] != y:
                    invert += 1

            if invert <= 2:
                print(invert)
                for r, c in a:
                    if A[r][c] != x:
                        print('{} {}'.format(r + 1, c + 1))
                for r, c in b:
                    if A[r][c] != y:
                        print('{} {}'.format(r + 1, c + 1))
                return



    T = int(input())
    for _ in range(T):
        N = int(input())
        A = []
        for _ in range(N):
            row = [int(x) if x not in {'S', 'F'} else 0 for x in input()]
            A.append(row)

        solve(A, N)

