# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def isValid(self, S: str) -> bool:
        q = []
        for v in S:
            if v == 'c':
                if len(q) >= 2 and q[-1] == 'b' and q[-2] == 'a':
                    q.pop()
                    q.pop()
            else:
                q.append(v)
        
        return not q
    
    
s = Solution()
print(s.isValid('aabcbc'))
print(s.isValid('abcabcababcc'))
print(s.isValid('abccba'))
print(s.isValid('cababc'))