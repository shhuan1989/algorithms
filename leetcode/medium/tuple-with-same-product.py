# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/19
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
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        count = collections.defaultdict(int)
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                count[nums[i] * nums[j]] += 1
        
        return sum(m*(m-1)*4 for m in count.values())

    
if __name__ == '__main__':
    s = Solution()
    print(s.tupleSameProduct([2,3,4,6]))
    print(s.tupleSameProduct([1,2,4,5,10]))
    print(s.tupleSameProduct([2,3,4,6,8,12]))
    print(s.tupleSameProduct([2,3,5,7]))