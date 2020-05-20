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
    def findBestValue(self, A: List[int], target: int) -> int:
        A.sort()
        N = len(A)
        presum = []
        for v in A:
            if not presum:
                presum.append(v)
            else:
                presum.append(presum[-1] + v)
                
        def getdiff(avg):
            i = bisect.bisect_right(A, avg)-1
            s = (presum[i] if 0 <= i < N else 0) + (N-i-1) * avg
            return abs(target - s)
            
        lo, hi = 0, max(A)
        while lo <= hi:
            if hi - lo < 2:
                if hi == lo:
                    return hi
                
                da, db = getdiff(lo), getdiff(hi)
                if da > db:
                    return hi
                
                return lo
            
            b = (lo + hi) // 2
            a, c = b-1, b+1
            da, db, dc = getdiff(a), getdiff(b), getdiff(c)
            if da > db and dc >= db:
                return b
            elif db >= dc:
                lo = c
            else:
                hi = a
            
            
            

    
s = Solution()
print(s.findBestValue([4,9,3], target = 10))
print(s.findBestValue([2,3,5], target = 10))
print(s.findBestValue([60864,25176,27249,21296,20204], target = 56803))