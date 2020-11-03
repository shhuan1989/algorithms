# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/22

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    
    MAXN = 200
    Row = [[0 for _ in range(200)] for _ in range(200)]
    Col = [[0 for _ in range(200)] for _ in range(200)]
    
    for _ in range(N):
        x, y = map(int, input().split())
        Row[x][y] += 1
        Col[x][y] += 1
    
    
    for i in range(1, 101):
        for j in range(1, 101):
            Col[i][j] += Col[i][j-1]
            Row[i][j] += Row[i-1][j]
    
    ans = 0
    for i in range(1, 100):
        for j in range(i+1, 101):
            mx = Col[1][j-1] - Col[1][i]
            for k in range(2, 101):
                ans = max(ans, Col[k][j-1] - Col[k][i] + Row[k][i] + Row[k][j] + mx)
                mx = max(mx, Col[k][j-1] - Col[k][i] - Row[k-1][i] - Row[k-1][j])
    
    print(ans)