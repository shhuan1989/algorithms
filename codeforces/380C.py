# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/30/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class SegmentTree:
    def __init__(self, N, s):
        self.matched = [0] * (4 * N + 1)
        self.left = [0] * (4 * N + 1)
        self.right = [0] * (4 * N + 1)
        self.N = N
        
        self.build(1, 1, N, s)
    
    def build(self, node, nodel, noder, s):
        if nodel == noder:
            a = 0
            b = 1 if s[nodel-1] == '(' else 0
            c = b ^ 1
            self.matched[node] = a
            self.left[node] = b
            self.right[node] = c
            return a, b, c
            
        mid = (nodel + noder) // 2
        a1, b1, c1 = self.build(node * 2, nodel, mid, s)
        a2, b2, c2 = self.build(node * 2 + 1, mid+1, noder, s)
        
        t = min(b1, c2)
        a = a1 + a2 + t
        b = b1 + b2 - t
        c = c1 + c2 - t
        
        self.matched[node] = a
        self.left[node] = b
        self.right[node] = c
        
        return a, b, c
        
    def query(self, l, r):
        a, b, c = self.query_impl(1, 1, self.N, l, r)
        return a * 2
    
    def query_impl(self, node, nodel, noder, targetl, targetr):
        if targetl > targetr or nodel > noder:
            return 0, 0, 0
        
        if nodel == targetl and noder == targetr:
            return self.matched[node], self.left[node], self.right[node]
        
        mid = (nodel + noder) // 2
        
        a1, b1, c1 = self.query_impl(node * 2, nodel, mid, targetl, min(mid, targetr))
        a2, b2, c2 = self.query_impl(node * 2 + 1, mid+1, noder, max(targetl, mid+1), targetr)
        
        t = min(b1, c2)
        a = a1 + a2 + t
        b = b1 + b2 - t
        c = c1 + c2 - t
        
        return a, b, c
        
  
def solve(s, q):
    N = len(s)
    t = SegmentTree(N, s)
    ans = [t.query(l, r) for l, r in q]
    print('\n'.join(map(str, ans)))


# import random
# s = ''
# for i in range(10**6):
#     if random.randint(1, 10) > 5:
#         s += '('
#     else:
#         s += ')'
# q = []
# for i in range(10**5):
#     l = random.randint(1, len(s))
#     r = random.randint(l, len(s))
#     q.append((l, r))
#
# print('starting...')
# t0 = time.time()
# solve(s, q)
# print(time.time() - t0)


s = input()
N = int(input())
q = []
for i in range(N):
    l, r = map(int, input().split())
    q.append((l, r))
solve(s, q)

