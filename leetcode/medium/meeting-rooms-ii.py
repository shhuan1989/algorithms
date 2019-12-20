# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        count = collections.defaultdict(int)
        for x, y in intervals:
            count[x] += 1
            count[y] -= 1
        
        ans = 0
        s = 0
        for x in sorted(count.keys()):
            s += count[x]
            ans = max(ans, s)
        
        return ans
        
        
    
s = Solution()
print(s.minMeetingRooms( [[0, 30],[5, 10],[15, 20]]))
print(s.minMeetingRooms([[7,10],[2,4]]))
