# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/25/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        mod = int(1e9 + 7)
        
        class Node:
            def __init__(self):
                self.p = -1
                self.c = []
                self.lazy = 0
                self.sum = 0
                self.size = 1
        
        p = [Node() for i in range(n)]
        for a, b in leadership:
            a -= 1
            b -= 1
            p[b].p = a
            p[a].c.append(b)
        
        def dfs(r):
            for c in p[r].c:
                p[r].size += dfs(c)
            return p[r].size
        
        for i in range(n):
            if p[i].p == -1:
                dfs(i)
        
        ans = []
        for op in operations:
            if len(op) == 3:
                o, n, l = op
            else:
                o, n = op
                l = None
            n -= 1
            if o == 1:
                c = n
                while c != -1:
                    p[c].sum += l
                    c = p[c].p
            elif o == 2:
                p[n].lazy += l
                c = n
                while c != -1:
                    p[c].sum += l * p[n].size
                    c = p[c].p
            else:
                c = p[n].p
                anc = []
                while c != -1:
                    anc.append(c)
                    c = p[c].p
                for a in anc[::-1]:
                    for c in p[a].c:
                        p[c].lazy += p[a].lazy
                        p[c].sum += p[a].lazy * p[c].size
                    p[a].lazy = 0
                ans.append(p[n].sum % mod)
        return ans
