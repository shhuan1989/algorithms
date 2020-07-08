# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/4

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

INF = 10**7

class SegmentTree:
    def __init__(self, size, useMax):
        n = size * 4 + 1
        v = -INF if useMax else INF
        self.data = [v for _ in range(n)]
        self.size = size
        self.n = n
        self.useMax = useMax
        self.lazy = [False for _ in range(n)]
    
    def push(self, index):
        pass
    
    def build(self):
        pass
    
    def update(self, index, val):
        self.update_impl(1, 0, self.size-1, index, index, val)
    
    def query(self, start, end):
        return self.query_impl(1, 0, self.size-1, start, end)
    
    def update_impl(self, index, nodel, noder, targetl, targetr, val):
        if nodel > noder or targetl > targetr:
            return -INF if self.useMax else INF
        
        self.push(index)
        if nodel == targetl and noder == targetr:
            self.data[index] = max(self.data[index], val) if self.useMax else min(self.data[index], val)
            return self.data[index]
        
        m = (nodel + noder) // 2
        a =  self.update_impl(index * 2, nodel, min(m, noder), targetl, min(m, targetr), val)
        b =  self.update_impl(index * 2 + 1, max(nodel, m+1), noder, max(targetl, m+1), targetr, val)
        c = max(a, b) if self.useMax else min(a, b)
        self.data[index] = max(self.data[index], c) if self.useMax else min(self.data[index], c)
        
        return c
        
    def query_impl(self, index, nodel, noder, targetl, targetr):
        if nodel > noder or targetl > targetr:
            return -INF if self.useMax else INF
    
        self.push(index)
        if nodel == targetl and noder == targetr:
            return self.data[index]
        
        m = (nodel + noder) // 2
        a = self.query_impl(index * 2, nodel, min(m, noder), targetl, min(m, targetr))
        b = self.query_impl(index * 2 + 1, max(m+1, nodel), noder, max(m+1, targetl), targetr)
        c = max(a, b) if self.useMax else min(a, b)
        
        return c
    
    
def solve(N, A):
    presum = [0]
    for v in A:
        presum.append(presum[-1] + v)
    
    left = []
    q = []
    # print(presum)
    st = SegmentTree(N, useMax=False)
    for i, v in enumerate(A):
        while q and q[-1][0] <= v:
            q.pop()
        j = q[-1][1] + 1 if q else 0
        left.append(max(presum[i] - st.query(j, i-1), 0))
        st.update(i, presum[i])
        q.append((v, i))
        # print(st.data)
        # print([st.query(i, i) for i in range(N+1)])
        
    right = []
    q = []
    st = SegmentTree(N, useMax=True)
    for i in range(N-1, -1, -1):
        v = A[i]
        while q and q[-1][0] <= v:
            q.pop()
        j = q[-1][1] - 1 if q else N-1
        right.append(max(0, st.query(i+1, j) - presum[i+1]))
        st.update(i, presum[i+1])
        q.append((v, i))
    right = right[::-1]
    
    # print(left)
    # print(right)
    
    return max([a+b for a, b in zip(left, right)])


def solve2(N, A):
    ans = 0
    INF = 10**9
    for mx in range(0, 31):
        curr, best = 0, 0
        for i, v in enumerate(A):
            curr += -INF if v > mx else v
            best = min(best, curr)
            ans = max(ans, (curr - best)  - mx)
    
    return ans


N = int(input())
A = [int(x) for x in input().split()]
# N = 10
# A = [-1 for _ in range(N)]
print(solve(N, A))
