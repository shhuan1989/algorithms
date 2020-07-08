# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        q = collections.defaultdict(int)
        hq = []
        ans = []
        
        a = []
        for l, r, h in buildings:
            a.append((l, h, 0))
            a.append((r, h, 1))
        
        a.sort()
        
        for pos, h, start in a:
            if start:
                q[h] -= 1
            else:
                q[h] += 1
                if q[h] == 1:
                    heapq.heappush(hq, -h)
            
            while hq and q[-hq[0]] == 0:
                heapq.heappop(hq)
                
            maxh = -hq[0] if hq else 0
            
            if not ans:
                ans.append([pos, maxh])
            elif ans[-1][0] == pos:
                ans[-1][1] = max(ans[-1][1], maxh)
            elif ans[-1][1] != maxh:
                ans.append([pos, maxh])
        
        return ans
    

s = Solution()
# print(s.getSkyline([[2,9,10],[9,12,15]]))
print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]))
                

            
        
        