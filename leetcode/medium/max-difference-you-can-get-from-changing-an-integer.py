# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maxDiff(self, num: int) -> int:
        
        s = list(str(num))
        
        vs = []
        for a in set(s):
            for b in range(10):
                v = [u if u != a else b for u in s]
                if v[0] != 0:
                    vs.append(int(''.join(map(str, v))))
        
        # print(vs)
        
        return max(vs) - min(vs)
        
s = Solution()
print(s.maxDiff(123435343))