# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = [[0] * (M+1)]
    for i in range(N):
        row = [0] + [int(x) for x in input().strip().split()]
        A.append(row)
    
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    def dfs(cx, cy, path, vis):
        if cx == ex and cy == ey:
            return ['->'.join(path)]
        
        ans = []
        for nx, ny in [(cx, cy-1), (cx-1, cy), (cx, cy+1), (cx+1, cy)]:
            if 1 <= nx <= N and 1 <= ny <= M and A[nx][ny] == 1 and (nx, ny) not in vis:
                ans += dfs(nx, ny, path + ['({},{})'.format(nx, ny)], vis | {(nx, ny)})
        return ans
    
    ans = dfs(sx, sy, ['({},{})'.format(sx, sy)], {(sx, sy)})
    if not ans:
        print(-1)
    else:
        print('\n'.join(ans))