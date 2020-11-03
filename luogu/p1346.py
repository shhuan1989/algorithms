# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N, S, T = map(int, input().split())
    
    dist = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        dist[i][i] = 0
    for u in range(1, N+1):
        row = [int(x) for x in input().split()]
        for i in range(1, len(row)):
            v = row[i]
            if i == 1:
                dist[u][v] = 0
            else:
                dist[u][v] = 1
    
    
    for k in range(1, N+1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    print(dist[S][T] if dist[S][T] < float('inf') else -1)
    
        