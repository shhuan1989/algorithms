# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/16 00:00

"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(endTime)
        jobs = [(endTime[i], startTime[i], profit[i], i) for i in range(N)]
        jobs.sort()

        dp = [0] * N
        dp[0] = jobs[0][2]
        for i in range(1, N):
            s, t = jobs[i][1], jobs[i][0]
            pre = bisect.bisect_left(jobs, (s, float('inf'), float('inf'), float('inf')))
            if 0 < pre < N:
                dp[i] = jobs[i][2] + dp[pre-1]
            else:
                dp[i] = jobs[i][2]
            dp[i] = max(dp[i], dp[i-1])

        return dp[N-1]

s = Solution()
print(s.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
print(s.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
print(s.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))
