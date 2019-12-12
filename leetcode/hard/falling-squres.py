# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/11/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class SegmentTree:
    def __init__(self, N):
        self.data = [0] * (4 * N + 2)
        self.lazy = [0] * (4 * N + 2)
        self.N = N
        
    def push(self, node):
        if self.lazy[node] > 0:
            l, r, v = node * 2, node * 2 + 1, self.lazy[node]
            self.lazy[l] += v
            self.lazy[r] += v
                
            self.lazy[node] = 0
        
    def update(self, left, right, add):
        return self.update_impl(1, 1, self.N, left, right, add)
    
    def update_impl(self, node, nodel, noder, targetl, targetr, add):
        if targetl > targetr:
            return self.data[node]
        
        if nodel == targetl and noder == targetr:
            self.lazy[node] += add
            self.data[node] += self.lazy[node]
            self.push(node)
            return self.data[node]
        else:
            self.push(node)
            m = (nodel + noder) // 2
            a = self.update_impl(node * 2, nodel, m, targetl, min(targetr, m), add)
            b = self.update_impl(node * 2 + 1, m + 1, noder, max(targetl, m+1), targetr, add)
            c = max(a, b)
            if c > self.data[node]:
                self.data[node] = c
                
            return self.data[node]
    
    def query(self, left, right):
        return self.query_impl(1, 1, self.N, left, right)
    
    def query_impl(self, node, nodel, noder, targetl, targetr):
        if targetl > targetr:
            return 0
        
        if nodel == targetl and noder == targetr:
            return self.data[node]
        
        self.push(node)
        m = (nodel + noder) // 2
        return max(self.query_impl(node * 2, nodel, m, targetl, min(targetr, m)),
                   self.query_impl(node * 2 + 1, m + 1, noder, max(targetl, m + 1), targetr))
    
    def max(self):
        return self.query(1, self.N)

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        st = SegmentTree(max([p+h for p, h in positions]))
        ans = []
        for left, width in positions:
            st.update(left, left+width-1, width)
            ans.append(st.max())

        return ans
    
s = Solution()
# print(s.fallingSquares([[1, 2], [2, 3], [6, 1]]))
print(s.fallingSquares([[9, 7], [1, 9], [3, 1]]))