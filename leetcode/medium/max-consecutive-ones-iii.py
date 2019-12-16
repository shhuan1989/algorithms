# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/12/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        zeros = [i for i in range(n) if A[i] == 0]
        if len(zeros) <= K:
            return n
        
        ans = max([zeros[i+1] - zeros[i] - 1 for i in range(len(zeros)-1)])
        ans = max(zeros[0], ans)
        ans = max(n-zeros[-1]-1, ans)
        for i in range(len(zeros)):
            j = i + K
            l = zeros[i-1] + 1 if i-1 >= 0 else 0
            r = zeros[j] if j < len(zeros) else n
            ans = max(ans, r-l)
        
        return ans
        
    def longestOnes2(self, A: List[int], K: int) -> int:
        ans, zero, l, r, n = 0, 0, 0, 0, len(A)
        while r < n:
            if A[r] == 0:
                zero += 1
            if zero <= K:
                ans = max(ans, r-l+1)
            else:
                while l <= r and zero > K:
                    if A[l] == 0:
                        zero -= 1
                    l += 1
                ans = max(ans, r-l+1)
            r += 1
        
        return ans
    
s = Solution()
print(s.longestOnes(A = [1,1,1,0,0,0,1,1,1,1,0], K = 2))
print(s.longestOnes(A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3))
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1], 0))
print(s.longestOnes([0,0,1,1,1,0,0], 0))
