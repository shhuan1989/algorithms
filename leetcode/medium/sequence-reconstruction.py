# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/18/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        
        vals = set()
        for s in seqs:
            vals |= set(s)
        
        if any([x not in vals for x in org]):
            return False
        
        
        g = collections.defaultdict(list)
        d = collections.defaultdict(int)
        for w in seqs:
            for i in range(len(w)-1):
                g[w[i]].append(w[i+1])
                d[w[i+1]] += 1
                
        q = [v for v in vals if d[v] == 0]
        if q != [org[0]]:
            return False
        
        restruct = []
        cur = q[0]
        while True:
            restruct.append(cur)
            q = []
            for v in g[cur]:
                d[v] -= 1
                if d[v] == 0:
                    q.append(v)
            if not q:
                break
            if len(q) > 1:
                return False
            cur = q[0]
        
        return restruct == org and len(restruct) == len(vals)
    
    
s = Solution()
print(s.sequenceReconstruction([1], [[1],[2,3],[3,2]]))
print(s.sequenceReconstruction([5,3,2,4,1], [[5,3,2,4],[4,1],[1],[3],[2,4], [1000000000]]))
# print(s.sequenceReconstruction([1, 3], [[1, 2], [1, 3]]))
# print(s.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3]]))
# print(s.sequenceReconstruction([1, 2, 3], [[1, 2]]))
# print(s.sequenceReconstruction([1, 2, 3], [[1, 2], [2, 3], [1, 3]]))
# print(s.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]))
# print(s.sequenceReconstruction([1], []))
