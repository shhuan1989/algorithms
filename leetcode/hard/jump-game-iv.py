# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def minJumps(self, A: List[int]) -> int:
        N = len(A)
        ans = [float('inf') for _ in range(N)]
        ans[0] = 0
        
        vi = collections.defaultdict(list)
        for i, v in enumerate(A):
            vi[v].append(i)
            
        q = [0]
        s = 1
        vis = set()
        while q:
            nq = []
            for i in q:
                for j in [i-1, i+1]:
                   if 0 <= j < N and ans[j] > s:
                       ans[j] = s
                       nq.append(j)
                if A[i] not in vis:
                    vis.add(A[i])
                    for j in vi[A[i]]:
                        if ans[j] > s:
                            ans[j] = s
                            nq.append(j)
            s += 1
            # print(q)
            q = nq
        # print(ans)
        return ans[-1]
        
        
s = Solution()
print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
print(s.minJumps([7]))
print(s.minJumps([7,6,9,6,9,6,9,7]))
print(s.minJumps( [6,1,9]))
print(s.minJumps([11,22,7,7,7,7,7,7,7,22,13]))
print(s.minJumps([7] * (5 * 10 ** 4) + [11]))