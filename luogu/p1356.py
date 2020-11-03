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
    M = int(input())
    for _ in range(M):
        N, K = map(int, input().split())
        A = [int(x) for x in input().split()]
        vis = [[False for _ in range(K)] for _ in range(2)]
        vis[0][A[0] % K] = True
        for i in range(1, N):
            v = A[i]
            for k in range(K):
                vis[i%2][k] = vis[(i+1)%2][(k-v)%K] or vis[(i+1)%2][(k+v)%K]
        
        if vis[(N+1)%2][0]:
            print('Divisible')
        else:
            print('Not divisible')
        
