# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    # sys.stdin = open('p1363.in', 'r')
    N, M = -1, -1
    A = []
    
    def solve():
        
        sr, sc = -1, -1
        for r in range(N):
            if sr >= 0:
                break
            for c in range(M):
                if A[r][c] == 'S':
                    sr = r
                    sc = c
                    break
        
        
        vis = [[0 for _ in range(M)] for _ in range(N)]
        vis2 = {(sr, sc)}
        vis[sr][sc] = 1
        q = [(sr, sc)]
        while q:
            r, c = q.pop()
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                xr = (nr + N) % N
                xc = (nc + M) % M
                if (nr, nc) in vis2:
                    continue
                vis2.add((nr, nc))
                if A[xr][xc] != '#':
                    if xr != nr or xc != nc and vis[xr][xc] > 0:
                        return True
                    if vis[xr][xc] < 2:
                        vis[xr][xc] += 1
                        q.append((nr, nc))
        
        return False
        
    
    for line in sys.stdin:
        if line[0].isdigit():
            if A:
                ans = solve()
                print('Yes' if ans else 'No')
            N, M = [int(x) for x in line.split()]
            A = []
        else:
            A.append(list(line))
    
    ans = solve()
    print('Yes' if ans else 'No')
    