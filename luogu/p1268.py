# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/14

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    ans = A[0][1]
    
    for i in range(2, N):
        d = min([(A[0][i] + A[i][j] - A[0][j])//2 for j in range(i)])
        ans += d
        
    return ans


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break
            
        A = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N-1):
            row = [int(x) for x in input().split()]
            for j, v in enumerate(reversed(row)):
                A[i][N-j-1] = v
                A[N-j-1][i] = v
        
        # for row in A:
        #     print(row)
        print(solve(N, A))
        