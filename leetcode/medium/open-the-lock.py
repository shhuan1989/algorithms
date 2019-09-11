# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        vis = set()
        deadends = {tuple([int(x) for x in d]) for d in deadends}
        
        s = (0, 0, 0, 0)
        if s in deadends:
            return -1
        t = tuple([int(x) for x in target])
        # print(t)
        q = [s]
        step = 0
        vis.add(s)
        
        while q:
            # print(q)
            nq = []
            for s in q:
                if s == t:
                    return step
                for ns in [((s[0]+1)%10, s[1], s[2], s[3]), ((s[0]+9)%10, s[1], s[2], s[3]),
                           (s[0], (s[1]+1) % 10, s[2], s[3]), (s[0], (s[1]+9)%10, s[2], s[3]),
                           (s[0], s[1], (s[2]+1)%10, s[3]), (s[0], s[1], (s[2]+9)%10, s[3]),
                           (s[0], s[1], s[2], (s[3]+1)%10), (s[0], s[1], s[2], (s[3]+9)%10)]:
                    if ns not in vis and ns not in deadends:
                        vis.add(ns)
                        nq.append(ns)
            q = nq
            step += 1
    
        return -1
    
s = Solution()
print(s.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))