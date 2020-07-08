# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/30

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(S, M, B):
    wc = collections.Counter(S)
    S = list(sorted(set(S), reverse=True))
    
    C = ['' for _ in range(M)]
    si = 0
    while True:
        fill = [i for i in range(M) if B[i] == 0]
        if not fill:
            break
        
        while wc[S[si]] < len(fill):
            si += 1
            
        for i in fill:
            C[i] = S[si]
            B[i] = -1
        for i in range(M):
            B[i] -= sum([abs(i-j) for j in fill])
        si += 1
    
    return ''.join(C)


if __name__ == '__main__':
    T = int(input())
    ans = []
    for ti in range(T):
        S = list(input())
        M = int(input())
        B = [int(x) for x in input().split()]
        ans.append(solve(S, M, B))
    
    print('\n'.join(ans))
        


    
    