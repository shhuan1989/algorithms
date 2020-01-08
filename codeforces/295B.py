# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/30/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

N = int(input())
A = []
for i in range(N):
    A.append([int(x) for x in input().split()])
S = [int(x) for x in input().split()]


def solve(N, A, S):
    nodes = []
    ans = []
    for node in reversed(S):
        node -= 1
        
        for i in nodes:
            for j in nodes:
                A[node][i] = min(A[node][i], A[node][j] + A[j][i])
                A[i][node] = min(A[i][node], A[i][j] + A[j][node])
        
        nodes.append(node)
        for i in nodes:
            for j in nodes:
                A[i][j] = min(A[i][j], A[i][node] + A[node][j])
                A[j][i] = min(A[j][i], A[j][node] + A[node][i])
        s = 0
        for u in nodes:
            for v in nodes:
                s += A[u][v]
        ans.append(s)
    
    return ans[::-1]
    
print(' '.join(map(str, solve(N, A, S))))
