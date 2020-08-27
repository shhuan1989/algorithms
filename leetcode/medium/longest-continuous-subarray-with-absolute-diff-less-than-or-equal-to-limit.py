# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/26

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        l, r = 0, 0
        minv, maxv = nums[0], nums[0]
        maxi, mini = 0, 0
        n = len(nums)
        
        asc = collections.deque([])
        desc = collections.deque([])
        while r < n:
            v = nums[r]
            
            while desc and nums[desc[-1]] < v:
                desc.pop()
            desc.append(r)
            
            while asc and nums[asc[-1]] > v:
                asc.pop()
            asc.append(r)
            
            if v > maxv:
                maxv = v
                maxi = r
            if v < minv:
                minv = v
                mini = r
            
            if maxv - minv > limit:
                if v == maxv:
                    while asc and maxv-nums[asc[0]] > limit:
                        asc.popleft()
                    minv = nums[asc[0]]
                    l = asc[0]
                    while l >= 0 and v - nums[l] <= limit:
                        l -= 1
                    l += 1
                else:
                    while desc and nums[desc[0]] - v > limit:
                        desc.popleft()
                    maxv = nums[desc[0]]
                    l = desc[0]
                    while l >= 0 and nums[l] - v <= limit:
                        l -= 1
                    l += 1
                    
                        
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans
    
if __name__ == '__main__':
    s = Solution()
    # print(s.longestSubarray([8,2,4,7], 4))
    # print(s.longestSubarray([10,1,2,4,7,2], 5))
    # print(s.longestSubarray([4,2,2,2,4,4,2,2], 0))
    
    print(s.longestSubarray([24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39],87))
    
    sys.stdin = open('1438.in', 'r')
    a = [int(x) for x in input().strip().split(',')]
    b = int(input())
    t0 = time.time()
    print(s.longestSubarray(a, b))
    print(time.time() - t0)