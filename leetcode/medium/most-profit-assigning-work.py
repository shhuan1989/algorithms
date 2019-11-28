# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/28/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


from typing import List


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = [(d, p) for d, p in zip(difficulty, profit)]
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

        
s = Solution()
print(s.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))