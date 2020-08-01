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
created by shhuan at 2020/7/19 17:37

"""

def solve(N, M, A):
    maxbi = -1
    maxb = float('-inf')
    A.sort(reverse=True)
    for i in range(M):
        if A[i][1] > maxb:
            maxb = A[i][1]
            maxbi = i
        if A[i][1] == maxbi and A[i][0] > A[maxbi][0]:
            maxbi = i

    presum = 0
    ans = A[maxbi][0] + maxb * (N-1)
    seen = False
    for i, (a, b) in enumerate(A):
        presum += a
        seen = seen or (i == maxbi)

        if N-i-2 < 0:
            break
        ans = max(ans, presum + ((N-i-1) * maxb if seen else (N-i-2)*maxb+A[maxbi][0]))

    return ans


if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        if ti > 0:
            input()
        N, M = map(int, input().split())
        A = []
        for i in range(M):
            a, b = map(int, input().split())
            A.append((a, b))

        ans.append(solve(N, M, A))



    print('\n'.join(map(str, ans)))

