# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        N = len(s)
        updown = []
        i, pv, upping = 0, 0, s[0] == 'I'
        for r, v in enumerate(s):
            if v == 'I':
                if upping:
                    pass
                else:
                    updown.append((i, r-1, 0))
                    i = r
                    upping = True
            else:
                if upping:
                    updown.append((i, r-1, 1))
                    i = r
                    upping = False
                else:
                    pass
        
        if upping:
            updown.append((i, N-1, 1))
        else:
            updown.append((i, N-1, 0))
        ans = [0] * (N+1)
        ans[0] = 1
        c = 2
        for l, r, u in updown:
            for i in range(l, r+1):
                ans[i+1] = c
                c += 1
            if not u:
                ans[l: r + 2] = ans[l: r + 2][::-1]
            
        return ans
        
        
        
        
        
        
s = Solution()
print(s.findPermutation('DDIIDI'))
print(s.findPermutation('IIDII'))
print(s.findPermutation('IDII'))
print(s.findPermutation('DIDD'))
print(s.findPermutation('IDD'))
print(s.findPermutation('D'))
print(s.findPermutation('I'))
print(s.findPermutation('DI'))
#