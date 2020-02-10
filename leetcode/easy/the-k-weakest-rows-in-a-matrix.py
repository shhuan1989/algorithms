# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/2/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a = []
        for i, row in enumerate(mat):
            v = sum(row)
            a.append((v, i))
        
        a.sort()
        
        return [v[1] for v in a[:k]]
    
s = Solution()
print(s.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))

print(s.kWeakestRows(mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))