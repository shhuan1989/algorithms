# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from functools import lru_cache
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # @lru_cache(maxsize=None)
        # def get(y):
        #     if y == 0:
        #         return 0, 0, 0
        #
        #     if y == 1:
        #         return 1, 1, 0
        #
        #     k = 0
        #     while 2 ** k <= y:
        #         k += 1
        #
        #     xa, xb, xc = y, y, 0
        #     for i in range(1, k):
        #         x = y // (2 ** i)
        #         rest = y - x * (2 ** i)
        #         a, b, c = get(x)
        #         if a + rest < xa:
        #             xa = a + rest
        #             xb = b + rest
        #             xc = c + i
        #         elif a + rest == xa and c < xc:
        #             xa = a + rest
        #             xb = b + rest
        #             xc = c + i
        #
        #     return xa, xb, xc
        
        
        def get(y):
            if y == 0:
                return 0, 0, 0
            
            if y & 1 > 0:
                a, b, c = get(y-1)
                return a+1, b+1, c
        
            a, b, c = get(y >> 1)
            return a+1, b, c+1
        
        ans = 0
        mul = 0
        for i, v in enumerate(nums):
            a, b, c = get(v)
            mul = max(mul, c)
            ans += b
        ans += mul
        
        return ans
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.minOperations([1, 5]))
    print(s.minOperations([2, 2]))
    print(s.minOperations([4, 2, 5]))
    print(s.minOperations([3, 2, 2, 4]))
    print(s.minOperations([2, 4, 8, 16]))
    print(s.minOperations([1000000000]))
    
    sys.stdin = open('1558.in', 'r')
    a = [int(x) for x in input().split(',')]
    t0 = time.time()
    print(s.minOperations(a))
    print(time.time() - t0)
    