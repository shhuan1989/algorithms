# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/11/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if sum(nums) % k != 0:
            return False
        
        t = sum(nums) // k
        
        def dfs(parts, vs):
            if not vs:
                print(parts)
                return True
            
            v = vs[0]
            vs = vs[1:]
            for i in range(k):
                if sum(parts[i] or [0]) + v <= t:
                    parts[i].append(v)
                    
                    if dfs(parts, vs):
                        return True
                    
                    parts[i].pop()
                    
                if not parts[i]:
                    break
                    
            return False
            
        nums.sort(reverse=True)
        return dfs([[] for _ in range(k)], nums)
        
        
        




s = Solution()

print(s.canPartitionKSubsets([4,15,1,1,1,1,3,11,1,10], 3))
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))

t0 = time.time()
print(s.canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 5))


print(time.time() - t0)