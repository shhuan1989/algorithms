# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/18/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for v in ops:
            if v == 'D':
                s.append((s[-1] if s else 0) * 2)
            elif v == 'C':
                if s:
                    s.pop()
            elif v == '+':
                s.append(sum(s[-2:]) if s else 0)
            else:
                s.append(int(v))
        
        return sum(s)
    
s = Solution()
print(s.calPoints(["5","2","C","D","+"]))
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))