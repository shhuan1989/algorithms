# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


INF = 10**6 + 5

class SegmentTree:
    def __init__(self, size, greater):
        self.greater = greater
        self.size = size
        self.n = size * 4
        self.data = [-INF if greater else INF for _ in range(self.n)]
        self.lazy = [False for _ in range (self.n)]
    
    def build(self, data):
        if not data:
            return
        self.size = len(data)
        self.n = self.size * 4
        self.data = [-INF if self.greater else INF for _ in range(self.n)]
        self.lazy = [False for _ in range(self.n)]
        
        for i in range(len(data)):
            self.update(i, i, data[i])
    
    def push(self, index):
        if index * 2 + 2 < self.n and self.lazy[index]:
            v = self.data[index]
            l = index * 2 + 1
            r = index * 2 + 2
            self.data[l] = max(self.data[l], v) if self.greater else min(self.data[l], v)
            self.data[r] = max(self.data[r], v) if self.greater else min(self.data[r], v)
            self.lazy[index] = False
            self.lazy[l] = True
            self.lazy[r] = True
            
    def update(self, l, r, val):
        self.update_impl(1, 0, self.size-1, l, r, val)
    
    def query(self, l, r):
        return self.query_impl(1, 0, self.size-1, l, r)
    
    def update_impl(self, index, nodel, noder, targetl, targetr, val):
        if nodel > noder or targetl > targetr or noder < targetl or nodel > targetr:
            return -INF if self.greater else INF
            
        if nodel == targetl and noder == targetr:
            self.data[index] = max(self.data[index], val) if self.greater else min(self.data[index], val)
            self.lazy[index] = True
            return self.data[index]
        
        self.push(index)
        m = (nodel + noder) // 2
        a = self.update_impl(index * 2 + 1, nodel, m, targetl, min(targetr, m), val)
        b = self.update_impl(index * 2 + 2, m + 1, noder, max(m + 1, targetl), targetr, val)
        self.data[index] = max(self.data[index], a, b) if self.greater else min(self.data[index], a, b)
        return self.data[index]
        
    
    def query_impl(self, index, nodel, noder, targetl, targetr):
        if nodel > noder or targetl > targetr or noder < targetl or nodel > targetr:
            return -INF if self.greater else INF
        
        if nodel == targetl and noder == targetr:
            return self.data[index]
        
        self.push(index)
        m = (nodel + noder) // 2
        a = self.query_impl(index * 2 + 1, nodel, m, targetl, min(m, targetr))
        b = self.query_impl(index * 2 + 2, m+1, noder, max(targetl, m+1), targetr)
        return max(a, b) if self.greater else min(a, b)
        

def dfs(k, xs, xy, segs):
    if k == 0:
        if not xs:
            return [segs]
        return []
    if not xs:
        return []
    
    ans = []
    miny, maxy = min(xy[xs[0]]), max(xy[xs[0]])
    for i in range(len(xs)):
        miny = min(miny, min(xy[xs[i]]))
        maxy = max(maxy, max(xy[xs[i]]))
        ans += dfs(k-1, xs[i+1:], xy, segs+[(xs[0], xs[i], miny, maxy)])

    return ans

def solve(N, K, points):
    points.sort()
    
    xs = list(sorted(set([x for x, y in points])))
    xy = collections.defaultdict(list)
    for x, y in points:
        xy[x].append(y)

    # MAXH = 1000
    # sa = SegmentTree(MAXH, True)
    # sb = SegmentTree(MAXH, False)
    #
    # for x, y in points:
    #     sa.update(x, x, y)
    #     sb.update(x, x, y)
    
    segs = dfs(K, xs, xy, [])
    ans = INF
    for seg in segs:
        area = 0
        for l, r, miny, maxy in seg:
            area += (r - l) * (maxy - miny)
            # area += (r - l) * (sa.query(l, r) - sb.query(l, r))
        # print(seg, area)
        ans = min(ans, area)
    
    return ans
    

if __name__ == '__main__':
    N, K = map(int, input().split())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    
    a = solve(N, K, points)
    b = solve(N, K, [(y, x) for x, y in points])
    print(min(a, b))