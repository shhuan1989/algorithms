# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 11/28/19

"""

import collections
import time
import os
import sys
import bisect
import heapq

from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        wc = collections.Counter(ages)
        uages = list(sorted(wc.keys()))
        
        return sum([((wc[a] * (wc[a]-1) if a >= 15 else 0) +
                    wc[a] * sum([wc[b] for b in uages[bisect.bisect_left(uages, a//2+8): bisect.bisect_right(uages, a-1)]])
                     ) if wc[a] > 0 else 0
                    for a in uages])
    
    
s = Solution()
print(s.numFriendRequests([16, 16]))
print(s.numFriendRequests([16,17,18]))
print(s.numFriendRequests([20,30,100,110,120]))
print(s.numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]))
print(s.numFriendRequests([109,6,101,18,13,20,106,110,110,108,55,89,81,56,84,37,71,51,88,70,27,16,31,63,99,68,12,120,104,18,110,42,93,106,99,63,3,82,22,17,69,49,88,117,57,37,95,15,50,18,77,103,102,104,87,1,23,97,93,15,9,35,59,103,118,23,52,66,86,7,40,33,60,4,113,43,21,58,31,120,71,56,19,67,68,32,84,14,50,55,98,34,89,32,58,20,93,37,95,40]))
import random
print(s.numFriendRequests([random.randint(1, 120) for _ in range(20000)]))

        
        
    