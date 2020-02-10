# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/15/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, A):
    # for each index i of each row, we count how many consecutive '1' right at i,
    # this is the max width if we include this row into the target submatrix which start from col i
    
    for r in range(N):
        for c in range(1, M):
            if A[r][c] != 0:
                A[r][c] = A[r][c-1] + 1
    ans = 0
    # we fix the right index of the sub-matrix, and scrub it to right
    heights = [0 for _ in range(M+1)]
    for right in range(M):
        # sort by O(N)
        for row in A:
            heights[row[right]] += 1
        count = 0
        for w in range(M+1):
            if heights[w] > 0:
                ans = max(ans, (N-count) * w)
                count += heights[w]
                heights[w] = 0
    
    print(ans)
    

N, M = map(int, input().split())
A = []
for i in range(N):
    row = [int(x) for x in list(input())]
    A.append(row)

solve(N, M, A)