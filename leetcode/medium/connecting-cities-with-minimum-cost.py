# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class UnionSet:
    def __init__(self):
        self.klen = collections.defaultdict(int)
        self.root = {}
    
    def uinon(self, u, v):
        pu, pv = self.find(u), self.find(v)
        kpu, kpv = max(self.klen[pu], 1), max(self.klen[pv], 1)
        
        if kpu < kpv:
            self.root[pu] = pv
            self.klen[pv] = kpu + kpv
        else:
            self.root[pv] = pu
            self.klen[pu] += kpu + kpv
    
    def find(self, u):
        if u not in self.root:
            return u
        parent = self.root[u]
        if parent < 0 or parent == u:
            return u
        
        ru = self.find(parent)
        self.root[u] = ru
        return ru
    
    def same(self, u, v):
        return self.find(u) == self.find(v)


class Solution:
    def minimumCost(self, N: int, conections: List[List[int]]) -> int:
        
        q = [(w, u, v) for u, v, w in conections]
        q.sort()
        ans = 0
        us = UnionSet()
        for w, u, v in q:
            if us.same(u, v):
                continue
            us.uinon(u, v)
            ans += w
        
        if all([us.find(u) == us.find(1) for u in range(2, N+1)]):
            return ans
            
        return -1
    
    
s = Solution()
print(s.minimumCost(N = 3, conections = [[1,2,5],[1,3,6],[2,3,1]]))
print(s.minimumCost(N = 4, conections = [[1,2,3],[3,4,4]]))



    
    