# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/10

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    N, M, A, B = map(int, input().strip().split())
    source = []
    for _ in range(A):
        x, y = map(int, input().split())
        source.append((x-1, y-1))
    target = []
    for _ in range(B):
        x, y = map(int, input().split())
        target.append((x-1, y-1))
    
    INF = M * N + 100
    T = [[INF for _ in range(M)] for _ in range(N)]
    q = collections.deque(source)
    for x, y in source:
        T[x][y] = 0
    while q:
        x, y = q.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and T[nx][ny] > T[x][y] + 1:
                T[nx][ny] = T[x][y] + 1
                q.append((nx, ny))
    
    for x, y in target:
        print(T[x][y])