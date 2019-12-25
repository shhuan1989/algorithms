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
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        presum = collections.defaultdict(int)
        presum[0] = 1
        s = 0
        for i, v in enumerate(A):
            s += v
            s %= K
            presum[s] += 1

        return sum([x*(x-1)//2 for x in presum.values()])
        
        
        

s = Solution()
print(s.subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5))