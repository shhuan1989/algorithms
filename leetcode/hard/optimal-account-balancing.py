# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/12/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def __init__(self):
        self.ans = float('inf')
        
    def minTransfers(self, transactions: List[List[int]]) -> int:
        self.ans = float('inf')
        debt = collections.defaultdict(int)
        for u, v, w in transactions:
            debt[u] += w
            debt[v] -= w
            
        borrower, lender = [abs(v) for v in debt.values() if v < 0], [v for v in debt.values() if v > 0]
        wca, wcb = collections.Counter(borrower), collections.Counter(borrower)
        borrower, lender, same = [], [], 0
        for k, c in wca.items():
            if k in wcb:
                borrower.extend([k] * max(0, c-wcb[k]))
                same += min(c, wcb[k])
            else:
                borrower.extend([k] * c)
        for k, c in wcb.items():
            if k in wca:
                lender.extend([k] * max(0, c-wca[k]))
            else:
                lender.extend([k] * c)
                
        def dfs(x, y, s):
            if not x:
                self.ans = min(self.ans, s)
                return 0
            
            if s > self.ans:
                return float('inf')
            
            ans = float('inf')
            for i in range(len(y)):
                if x[0] > y[i]:
                    ans = min(ans, 1 + dfs([x[0]-y[i]] + x[1:], y[:i] + y[i+1:], s+1))
                elif x[0] == y[i]:
                    ans = min(ans, 1 + dfs(x[1:],  y[:i] + y[i+1:], s + 1))
                else:
                    ans = min(ans, 1 + dfs(x[1:], y[:i] + [y[i]-x[0]] + y[i+1:], s + 1))
            
            return ans
        
        return dfs(borrower, lender, 0) + same
        

s = Solution()
print(s.minTransfers([[0, 1, 10], [2, 0, 5]]))
print(s.minTransfers([[0, 1, 10], [2, 0, 5], [1, 2, 3]]))
print(s.minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]]))
print(s.minTransfers([[0,1,1],[0,2,1],[1,3,1],[2,3,1]]))
print(s.minTransfers([[0,3,2],[1,4,3],[2,3,2],[2,4,2]]))