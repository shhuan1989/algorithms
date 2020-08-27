# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/24

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        if satisfaction[0] >= 0:
            return sum([(i + 1) * v for i, v in enumerate(satisfaction)])
        
        ns = len(satisfaction)
        suffix = [0 for _ in range(ns+1)]
        for i in range(ns-1, -1, -1):
            suffix[i] = suffix[i+1] + satisfaction[i]
        
        
        ans = 0
        score = 0
        for s in range(ns-1, -1, -1):
            score += suffix[s]
            ans = max(ans, score)
        
        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.maxSatisfaction([-2,5,-1,0,3,-3]))
    print(s.maxSatisfaction([-1,-8,0,5,-9]))
