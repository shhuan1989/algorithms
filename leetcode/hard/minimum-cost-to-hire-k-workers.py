# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        workers = [(Fraction(w, q), q, w) for q, w in zip(quality, wage)]
        workers.sort()
        print(workers)
        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)
    
    
s = Solution()
print(s.mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], K = 2))