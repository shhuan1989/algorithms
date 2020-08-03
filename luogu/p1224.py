# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/28

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import random

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    
    A = []
    for i in range(N):
        row = [int(x) % K for x in input().split()]
        A.append(row)
    
    rowid = [i for i in range(N)]
    
    def check(r1, r2):
        return sum([a*b for a, b in zip(A[r1], A[r2])]) % K == 0
    
    for epoch in range(4):
        random.shuffle(rowid)
        presum = [0 for _ in range(M)]
        
        for i in range(N):
            r = rowid[i]
            for c in range(M):
                if K == 2:
                    presum[c] ^= A[r][c]
                else:
                    presum[c] *= A[r][c] * A[r][c]
                    presum[c] %= K
                    
            if sum(presum) % K != i % K:
                for j in range(i):
                    if check(rowid[i], rowid[j]):
                        r1, r2 = rowid[i], rowid[j]
                        r1, r2 = min(r1, r2), max(r1, r2)
                        print('{} {}'.format(r1+1, r2+1))
                        exit(0)
                        
    print(-1)
