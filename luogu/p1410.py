# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/5

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


if __name__ == '__main__':
    
    def solve(A):
        N = len(A)
        
        uniq = list(sorted(set(A)))
        vi = {v:i for i, v in enumerate(uniq)}
        A = [vi[v] for v in A]
        
        bits = [0 for _ in range(N+1)]
        
        def update(index, val):
            while index <= N:
                bits[index] = max(bits[index], val)
                index |= index + 1
                
        def query(index):
            s = 0
            while index >= 0:
                s = max(s, bits[index])
                index = (index & (index + 1)) - 1
            return s
        
        A = A[::-1]
        for i in range(N):
            pre = query(A[i] - 1)
            if pre + 1 > 2:
                return False
            update(A[i], pre + 1)
            
        return True
        
        
        
        
    
    for line in sys.stdin.readlines():
        A = [int(x) for x in line.split()][1:]
        print('Yes!' if solve(A) else 'No!')
    # A = [float('-inf')] + [int(x) for x in input().split()][1:]
    # print(solve(A))