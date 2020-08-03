# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/3

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
    A = list(input().strip())
    A += A
    B = []
    w, c = A[0], 1
    for i in range(1, 2*N):
        if A[i] != w:
            B.append((w, c))
            w = A[i]
            c = 1
        else:
            c += 1
    # B.append((w, c))
    # print(''.join(A))
    # print(B)
    
    if len(set(A)) == 1:
        print(N)
        exit(0)
        
    ans = 1
    for i, (w, c) in enumerate(B):
        if w == 'w':
            continue
        s = i - 1
        while s >= 0 and B[s][0] == 'w':
            s -= 1
        s += 1
        j = i
        while j < len(B) and (B[j][0] == 'w' or B[j][0] == B[i][0]):
            j += 1
        k = j
        while k < len(B) and (B[k][0] == 'w' or B[k][0] != B[i][0]):
            k += 1

        s = sum([v[1] for v in B[s: k]])
        # print(B[i: k], s)
        ans = max(ans, s)
    ans = min(ans, N)
    print(ans)
