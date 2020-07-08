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
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        vis = set()
        least = collections.defaultdict(int)
        
        for v in names:
            if v not in vis:
                vis.add(v)
                ans.append(v)
                least[v] = 1
            else:
                i = max(least[v], 1)
                while True:
                    u = '{}({})'.format(v, i)
                    if u not in vis:
                        vis.add(u)
                        ans.append(u)
                        break
                    i += 1
                least[v] = i
        
        return ans
    
    
s = Solution()
print(s.getFolderNames(["pes","fifa","gta","pes(2019)"]))
print(s.getFolderNames(["gta","gta(1)","gta","avalon"]))
print(s.getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
print(s.getFolderNames(["wano","wano","wano","wano"]))
print(s.getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]))
