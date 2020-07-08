# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # print(len(rains))
        wi = collections.defaultdict(list)
        for i, v in enumerate(rains):
            if v > 0:
                wi[v].append(i)
        
        full = set()
        q = []
        
        INF = len(rains) + 1
        ans = []
        for i, v in enumerate(rains):
            if v > 0:
                if v in full:
                    return []

                j = bisect.bisect_right(wi[v], i)
                if 0 <= j < len(wi[v]):
                    full.add(v)
                    heapq.heappush(q, (wi[v][j], v))
                ans.append(-1)
            elif v == 0:
                if q:
                    index, remove = heapq.heappop(q)
                    full.remove(remove)
                    ans.append(remove)
                else:
                    ans.append(1)

        return ans
    
    
s = Solution()
print(s.avoidFlood([1, 2, 3, 4]))
print(s.avoidFlood([1,2,0,0,2,1]))
print(s.avoidFlood([1,2,0,1,2]))
print(s.avoidFlood([69,0,0,0,69]))
print(s.avoidFlood([10,20,20]))
