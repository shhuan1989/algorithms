# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/4/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        a = [i+1 for i in range(m)]
        ans = []
        for v in queries:
            i = a.index(v)
            ans.append(i)
            a = [v] + a[:i] + a[i+1:]
            # print(a)
        
        return ans
    
s = Solution()
print(s.processQueries([3, 1, 2, 1], 5))
print(s.processQueries([4, 1, 2, 2], 4))