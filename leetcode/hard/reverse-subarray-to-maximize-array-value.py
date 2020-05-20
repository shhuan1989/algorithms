# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/4/22

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        #获得不反转后者整个数组翻转的[数组值]
        sumD = sum([abs(nums[i] - nums[i-1]) for i in range(1, len(nums))])

        a = max([min(nums[i], nums[i-1]) for i in range(1, len(nums))]) # 获得减项的最大值
        b = min([max(nums[i], nums[i-1]) for i in range(1, len(nums))]) #获得加项的最小值
        d = 0
        for i in range(1, len(nums)): # 对头尾进行处理, 参考暴力解法
            d = max(d, abs(nums[i] - nums[0]) - abs(nums[i-1]- nums[i]))
            d = max(d, abs(nums[i-1] - nums[-1]) - abs(nums[i] - nums[i-1]))
        #这里没有判读a, b之间的大小关系, 如果a < b 那么, 2a-2b一定小于d, 没有必要判断
        return sumD + max(2*a - 2*b, d)
            
            
s = Solution()
print(s.maxValueAfterReverse([2, 3, 1, 5, 4]))
print(s.maxValueAfterReverse([2, 4, 9, 24, 2, 1, 10]))