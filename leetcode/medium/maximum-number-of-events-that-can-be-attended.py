# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/16/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0
        
        q = []
        mx = max([r for l, r in events]) + 1
        
        s = collections.defaultdict(list)
        for l, r in events:
            s[l].append(r)
        
        ans = 0
        for i in range(mx):
            for r in s[i]:
                heapq.heappush(q, r)
            
            while q and q[0] < i:
                heapq.heappop(q)
            
            if q:
                heapq.heappop(q)
                ans += 1
               
        return ans
 
    
s = Solution()
print(s.maxEvents([[1,2],[2,3],[3,4]]))
print(s.maxEvents([]))
print(s.maxEvents([[1,2],[2,3],[3,4],[1,2]]))
print(s.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))
print(s.maxEvents( [[1,100000]]))
print(s.maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]))
print(s.maxEvents([[1,2],[1,2],[1,6],[1,2],[1,2]]))
print(s.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]]))
print(s.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]]))

