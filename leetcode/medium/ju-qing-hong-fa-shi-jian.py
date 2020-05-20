# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/4/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        n = len(requirements)
        
        ta = [-1 if requirements[i][0] > 0 else 0 for i in range(n)]
        tb = [-1 if requirements[i][1] > 0 else 0 for i in range(n)]
        tc = [-1 if requirements[i][2] > 0 else 0 for i in range(n)]
        
        ra = [(v[0], i) for i, v in enumerate(requirements)]
        rb = [(v[1], i) for i, v in enumerate(requirements)]
        rc = [(v[2], i) for i, v in enumerate(requirements)]
        
        ra.sort()
        rb.sort()
        rc.sort()
        
        ia, ib, ic = 0, 0, 0
        ca, cb, cc = 0, 0, 0
        
        while ia < n and ra[ia][0] <= 0:
            ia += 1
        while ib < n and rb[ib][0] <= 0:
            ib += 1
        while ic < n and rc[ic][0] <= 0:
            ic += 1
        
        for i, (a, b, c) in enumerate(increase):
            ca += a
            cb += b
            cc += c
            
            while ia < n and ra[ia][0] <= ca:
                ta[ra[ia][1]] = max(ta[ra[ia][1]], i + 1)
                ia += 1
            
            while ib < n and rb[ib][0] <= cb:
                tb[rb[ib][1]] = max(tb[rb[ib][1]], i + 1)
                ib += 1
            
            while ic < n and rc[ic][0] <= cc:
                tc[rc[ic][1]] = max(tc[rc[ic][1]], i + 1)
                ic += 1
        
        return [max(a, b, c) if a >= 0 and b >= 0 and c >= 0 else -1 for a, b, c in zip(ta, tb, tc)]

    
s = Solution()
print(s.getTriggerTime(increase = [[2,8,4],[2,5,0],[10,9,8]], requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]))
print(s.getTriggerTime(increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]], requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]))
print(s.getTriggerTime([[1,1,1]], [[0,0,0]]))


        
        