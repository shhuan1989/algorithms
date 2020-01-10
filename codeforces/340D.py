# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/8/20


Use fenwick tree to solve longest increasing sequence

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    bit = [0 for _ in range(N)]
    
    def add(index, val):
        while index < N:
            bit[index] = max(bit[index], val)
            index |= index + 1
            
    def query(index):
        s = 0
        index = min(index, N-1)
        while index >= 0:
            s = max(bit[index], s)
            index = (index & (index + 1)) - 1
        return s
        
    q = [(v, i) for i, v in enumerate(A)]
    q.sort()
    ans = 0
    for v, i in q:
        add(i, query(i-1) + 1)
        ans = max(ans, query(i))
    
    return ans



# def test():
#     N = 10**5
#     import random
#     for i in range(10):
#         A = [random.randint(1, 10 ** 3) for _ in range(N)]
#         t0 = time.time()
#         print(solve(N, A))
#         print(time.time() - t0)
#
# test()
    
N = int(input())
A = [int(x) for x in input().split()]
print(solve(N, A))