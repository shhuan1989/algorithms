# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/23/19

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
        N = 10 ** 5
        mark = [True] * N
        mark[0] = mark[1] = False
        for i in range(2, N):
            if mark[i]:
                v = i + i
                while v < N:
                    mark[v] = False
                    v += i
                    
        self.primes = [i for i in range(N) if mark[i]]
    
    def getFactors(self, n: int) -> List[List[int]]:
        target = n
        factors = collections.defaultdict(int)
        
        for d in self.primes:
            if d > n:
                break
            while n % d == 0:
                n //= d
                factors[d] += 1
        
        if n > 1:
            factors[n] += 1
        
        wc = [(w, c) for w, c in factors.items()]
        # print(wc)
        
        def partial(index, val):
            if index >= len(wc):
                return [val] if val > 1 else []
                
            ans = []
            w, c = wc[index]
            for i in range(0, c+1):
                ans.extend(partial(index+1, val * (w ** i)))
                
            return ans
        
        ps = partial(0, 1)
        ps.sort()
        
        # print(len(ps))

        def dfs(index, val, pre):
            if val == target:
                return [pre]  if len(pre) > 1 else []
            if index >= len(ps):
                return []
            
            if target % val != 0:
                return []
            
            rest = target // val
            if pre and rest < pre[-1]:
                return []
            
            ans = []
            
            for i in range(index, len(ps)):
                if val * ps[i] > target:
                    break
                c = 1
                while True:
                    nv = val * (ps[i] ** c)
                    if nv > target:
                        break
                    ans.extend(dfs(i+1, nv, pre+[ps[i] for _ in range(c)]))
                    c += 1
            
            return ans
        
        
        return dfs(0, 1, [])
        
        
s = Solution()
print(s.getFactors(8193))
print(s.getFactors(12))
print(s.getFactors(11))
print(s.getFactors(8))
print(s.getFactors(32))
t0 = time.time()
print(s.getFactors(10**9))
print(time.time() - t0)