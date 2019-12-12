# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/9/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        if K < 1:
            return -1
        
        ans = 1
        rem = 1
        while rem < K:
            rem *= 10
            rem += 1
            ans += 1
        
        while True:
            dk = K
            for x in range(1, 10):
                if (K * x) % 10 == rem % 10:
                    dk = K * x
                    break
            
            if dk % 10 != rem % 10:
                return -1
            
            tk, tv = 0, rem
            while tv > 0:
                tk += 1
                tv //= 10
                
            while rem < dk:
                rem = 10 ** tk + rem
                ans += 1
                tk += 1
            
            if rem == dk:
                break
            
            rem -= dk
            
            if rem % K == 0:
                break
            
            rem = 10 ** tk + rem
            ans += 1
            while rem > 0 and rem % 10 == 0:
                rem //= 10
        
        return ans
        
            
            
s = Solution()
print(s.smallestRepunitDivByK(3))
print(s.smallestRepunitDivByK(13))
print(s.smallestRepunitDivByK(2))
print(s.smallestRepunitDivByK(1))
print(s.smallestRepunitDivByK(71))
