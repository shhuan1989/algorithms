# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/24
"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        n = len(quantity)
        wc = collections.Counter(nums)
        wc = list(wc.values())
        m = len(wc)
        dp = [[False for _ in range(1 << n)] for _ in range(m)]
        
        @lru_cache(maxsize=None)
        def state2index(s):
            return [i for i in range(n) if (s & (1 << i)) > 0]
        
        @lru_cache(maxsize=None)
        def getpreviousstate(s):
            idx = state2index(s)
            ans = []
            for i in range(1 << len(idx)):
                ps = 0
                for j in range(len(idx)):
                    if (i & (1 << j)) > 0:
                        ps |= 1 << idx[j]
                ans.append(ps)
            
            return ans
        
        @lru_cache(maxsize=None)
        def getdiff(sa, sb):
            s = 0
            for i in range(n):
                if (sa & (1 << i)) > 0 and (sb & (1 << i)) == 0:
                    s |= 1 << i
            return s
        
        @lru_cache(maxsize=None)
        def getrequirement(s):
            return sum([quantity[i] for i in range(n) if (s & (1 << i)) > 0])
        
        for s in range(1 << n):
            dp[0][s] = getrequirement(s) <= wc[0]
        
        for i in range(1, m):
            for s in range(1 << n):
                if dp[i - 1][s]:
                    dp[i][s] = True
                    continue
                
                dp[i][s] = any(dp[i - 1][ps] and wc[i] >= getrequirement(getdiff(s, ps)) for ps in getpreviousstate(s))
                # for ps in getpreviousstate(s):
                #     if not dp[i - 1][ps]:
                #         continue
                #     curr = getdiff(s, ps)
                #     if wc[i] >= sum([quantity[j] for j in curr]):
                #         dp[i][s] = True
                #         break
        return dp[-1][(1 << n) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.canDistribute(nums=[1, 2, 3, 4], quantity=[2]))
    print(s.canDistribute(nums=[1, 2, 3, 3], quantity=[2]))
    print(s.canDistribute(nums=[1, 1, 2, 2], quantity=[2, 2]))
    print(s.canDistribute(nums=[1, 1, 2, 3], quantity=[2, 2]))
    print(s.canDistribute(nums=[1, 1, 1, 1, 1], quantity=[2, 3]))
