# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List



class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = collections.defaultdict(list)
        for u, v in tickets:
            g[u].append(v)
            print(u, v)
        
        for u in g.keys():
            g[u].sort()
            
        
        ans = []
        
        def hierholzer(curr):
            while g[curr]:
                v = g[curr].pop(0)
                hierholzer(v)
            ans.append(curr)
        
        hierholzer('JFK')
        
        return ans[::-1]

    
if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["JFK","ZUL"],["JFK","NRT"],["NRT","JFK"]]))
    # print(s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    # print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))