# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/20

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
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
        
    M = max(A)
    mark = [False for _ in range(M+1)]
    for a in A:
        for b in A:
            mark[abs(a-b)] = True
    
    K = N
    while True:
        if not mark[K]:
            u = K + K
            find = True
            while u <= M:
                if mark[u]:
                    find = False
                    break
                u += K
            if find:
                print(K)
                exit(0)
        K += 1