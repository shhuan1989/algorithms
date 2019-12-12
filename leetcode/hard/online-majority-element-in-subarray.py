# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/11/19

1. 线段树计算每个区间可能得最大的数字 o(logN)，摩尔投票
2. 统计这个数字在这个区间的个数 O(logN)

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.data = [(0, 0)] * (4*n + 1)
        self.build(1, 0, n-1, arr)
        self.n = n
        
    def build(self, node, nodel, noder, arr):
        if nodel > noder:
            return (0, 0)
        if nodel == noder:
            self.data[node] = (arr[nodel], 1)
            return (arr[nodel], 1)
        
        m = (nodel + noder) // 2
        a = self.build(node * 2, nodel, m, arr)
        b = self.build(node * 2 + 1, m+1, noder, arr)
        
        ans = (0, 0)
        if a[0] == b[0]:
            ans = (a[0], a[1] + b[1])
        elif a[1] > b[1]:
            ans = (a[0], a[1] - b[1])
        else:
            ans = (b[0], b[1] - a[1])
        
        self.data[node] = ans
        return ans
        
        
    def query(self, targetl, targetr):
        return self.query_impl(1, 0, self.n-1, targetl, targetr)
    
    def query_impl(self, node, nodel, noder, targetl, targetr):
        if nodel == targetl and noder == targetr:
            return self.data[node]
        
        if targetl > targetr:
            return (0, 0)
        
        m = (nodel + noder) // 2
        a = self.query_impl(2 * node, nodel, m, targetl, min(targetr, m))
        b = self.query_impl(2 * node + 1, m+1, noder, max(targetl, m+1), targetr)
        
        if a[0] == b[0]:
            return (a[0], a[1] + b[1])
        elif a[1] > b[1]:
            return (a[0], a[1] - b[1])
        else:
            return (b[0], b[1] - a[1])
        
        

class MajorityChecker:
    
    def __init__(self, arr: List[int]):
        # self.st = SegmentTree(arr)
        idx = collections.defaultdict(list)
        
        for i, v in enumerate(arr):
            idx[v].append(i)
        
        # self.idx = idx
        self.idx = sorted([*idx.items()], key=lambda x: -len(x))
        
        
        
    def query(self, left: int, right: int, threshold: int) -> int:
        
        for num, ix in self.idx:
            if (len(ix)) >= threshold:
                l_idx = bisect.bisect_left(ix, left)
                r_idx = bisect.bisect(ix, right)
                if r_idx - l_idx >= threshold:
                    return num
            else:
                break
        return -1
        
        
        # a, c = self.st.query(left, right)
        # ix = self.idx[a]
        # if ix:
        #     l, r = bisect.bisect_left(ix, left), bisect.bisect_right(ix, right)
        #     d = r - l
        #     if d >= threshold:
        #         return a
        #
        # return -1
        
        
    
    
m = MajorityChecker([1,1,2,2,1,1])
print(m.query(0, 5, 4))
print(m.query(0, 3, 3))
print(m.query(2, 3, 2))

# [null,-1,1,-1,-1,-1,2,-1,-1,-1,1]
m = MajorityChecker([])
for op, param in zip(["MajorityChecker","query","query","query","query","query","query","query","query","query","query"], [[2,1,1,1,2,1,2,1,2,2,1,1,2],[2,9,7],[9,11,2],[2,11,7],[3,4,2],[0,1,2],[6,9,3],[3,12,7],[3,10,6],[7,11,4],[0,6,4]]):
    if op == 'MajorityChecker':
        m = MajorityChecker(param)
    elif op == 'query':
        print(m.query(param[0], param[1], param[2]))
    