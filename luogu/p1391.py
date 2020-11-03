# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


if __name__ == '__main__':
    
    N = int(input())
    A = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        A.append(row)

    INF = 10000
    
    def check(row):
        if row >= N:
            return 0
        updated = []
        for c in range(N):
            neb = [(x, y) for x, y in [(row-1, c), (row+1, c), (row, c-1), (row, c+1)] if 0 <= x < N and 0 <= y < N]
            boy = sum(A[x][y] for x, y in neb)
            if boy % 2 != 0:
                if row + 1 >= N or A[row+1][c] == 1:
                    return INF
                updated.append(c)
        
        if updated and row+1 >= N:
            return INF
        
        for c in updated:
            A[row+1][c] = 1
        ans = len(updated) + check(row + 1)
        for c in updated:
            A[row+1][c] = 0
        return ans
    
    
    ans = INF
    for first in range(2**N):
        if any(A[0][c] == 1 and (first & (1 << c)) == 0 for c in range(N)):
            continue
        
        updated = [c for c in range(N) if first & (1 << c) > 0 and A[0][c] == 0]
        for c in updated:
            A[0][c] = 1
        
        ans = min(ans, len(updated) + check(0))
        
        for c in updated:
            A[0][c] = 0
    
    print(ans if ans < INF else -1)