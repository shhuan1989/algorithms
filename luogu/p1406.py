# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/23

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
    A = [int(x) for x in input().split()]
    
    sa = sum(A)
    avg = sum(A) // N
    
    
    mat = [[0 for _ in range(N)] for _ in range(N)]
    
    A.sort()
    
    print(avg)
    def dfs(r, c, rest):
        if r >= N:
            if sum([mat[x][x] for x in range(N)]) == avg and sum([mat[x][N-x-1] for x in range(N)]) == avg:
                for row in mat:
                    print(' '.join(map(str, row)))
                
                exit(0)
        
        if c == 0 and r > 0:
            prerow = sum(mat[r-1])
            if prerow != avg:
                return
        
        if r == N-1 and c > 0:
            precol = sum([mat[x][c-1] for x in range(N)])
            if precol != avg:
                return
        
        nr, nc = (r, c+1) if c + 1 < N else (r+1, 0)
        for i, v in enumerate(rest):
            mat[r][c] = v
            dfs(nr, nc, rest[:i] + rest[i+1:])
            mat[r][c] = 0
    
    dfs(0, 0, A)