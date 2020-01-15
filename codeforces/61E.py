# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/13/20

find the count of i, j, k that i < j < k and A[i] > A[j] > A[k]

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve_seg(N, A):
    vi = [(v, i) for i, v in enumerate(A)]
    vi.sort()
    B = [0 for _ in range(N)]
    for u, (v, i) in enumerate(vi):
        B[i] = u
    
    SegmentTree = [0 for _ in range(4 * N)]
    
    def add(index, val):
        add_impl(1, 0, N-1, index, index, val)
        
    def add_impl(index, nodel, noder, targetl, targetr, val):
        if targetl > targetr:
            return
        if nodel == targetl and noder == targetr:
            SegmentTree[index] += val
        else:
            m = (nodel + noder) // 2
            add_impl(index * 2, nodel, m, targetl, min(m, targetr), val)
            add_impl(index * 2 + 1, m + 1, noder, max(targetl, m + 1), targetr, val)
            SegmentTree[index] += val
            
    def query(val, greater):
        return query_impl(1, 0, N-1, val + 1, N-1)
    
    def query_impl(index, nodel, noder, targetl, targetr):
        if targetl > targetr:
            return 0
        
        if nodel == targetl and noder == targetr:
            return SegmentTree[index]

        m = (nodel + noder) // 2
        s = query_impl(index * 2, nodel, m, targetl, min(targetr, m))
        s += query_impl(index * 2 + 1, m + 1, noder, max(targetl, m + 1), targetr)
        return s
    
    ans = 0
    for i, v in enumerate(B):
        add(v, 1)
        a = query(v, True)
        b = v - (i - a)
        ans += a * b
        
    return ans
    

def solve(N, A):
    # values in A are distinct, so map them to [0, N-1]
    vi = [(v, i) for i, v in enumerate(A)]
    vi.sort()
    B = [0 for _ in range(N)]
    for u, (v, i) in enumerate(vi):
        # map to N-u-1 so that we need find i < j < k and A[i] < A[j] < A[k]
        B[i] = N - u - 1
    
    bit = [0 for _ in range(N)]
    
    def add(index, val):
        while index < N:
            bit[index] += val
            index |= index + 1
            
    def query(index):
        index = min(index, N-1)
        s = 0
        while index >= 0:
            s += bit[index]
            index = (index & (index + 1)) - 1
        return s
    
    ans = 0
    for i, v in enumerate(B):
        # for each v, find the count of values that on the left of v and greater than v
        a = query(v-1)
        # also find the count of values that on the right of v and less than v
        b = (N-v-1) - (i-a)
        ans += a * b
        add(v, 1)
    
    return ans


def test():
    import random
    N = 10**6
    A = [random.randint(0, 10**9) for _ in range(N)]
    t0 = time.time()
    print('starting')
    # print(solve_seg(N, A))
    print(solve(N, A))
    print(time.time() - t0)
 
 
# test()
    
N = int(input())
A = [int(x) for x in input().split()]
print(solve(N, A))