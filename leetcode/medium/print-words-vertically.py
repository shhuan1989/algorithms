# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        if not s:
            return []
        
        a = [v.strip() for v in s.split()]
        n = len(a)
        m = max([len(x) for x in a] or [0])
        
        ans = [[' ' for _ in range(n)] for _ in range(m)]
        
        for i, v in enumerate(a):
            for j, u in enumerate(v):
                ans[j][i] = u
                
        
        return [''.join(row).rstrip() for row in ans]
    

s = Solution()
print(s.printVertically("HOW ARE YOU"))
print(s.printVertically("TO BE OR NOT TO BE"))
print(s.printVertically( "CONTEST IS COMING"))
            