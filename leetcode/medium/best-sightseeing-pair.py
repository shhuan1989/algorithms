# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/2/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        c = A[-1] - N + 1
        ans = float('-inf')
        for i in range(N-2, -1, -1):
            ans = max(ans, A[i]+i+c)
            c = max(A[i] - i, c)
        
        return ans

s = Solution()
print(s.maxScoreSightseeingPair([8,1,5,2,6]))