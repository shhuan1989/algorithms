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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        edges = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort()
        
        parent = [i for i in range(n + 1)]
        
        def find(u):
            if u == parent[u]:
                return u
            pu = find(parent[u])
            parent[u] = pu
            
            return pu
        
        def merge(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
                return True
            return False
        
        def clean():
            for i in range(n + 1):
                parent[i] = i
        
        def minspan(edges, exclude, maxdist):
            clean()
            dist = 0
            for w, u, v, i in edges:
                # do not select this one
                if i == exclude:
                    continue
                if merge(u, v):
                    dist += w
                    if dist > maxdist:
                        return dist
            
            return dist
        
        mindist = minspan(edges, -1, float('inf'))
        critical = set()
        for i in range(len(edges)):
            # is remove the i-th edge, we getter a larger span tree, that means it is a critical one
            if minspan(edges, i, mindist) != mindist:
                critical.add(i)
        
        others = []
        for i in range(len(edges)):
            # select i-th edge and re-calculate the min span tree
            # put the i-th edge in front of list, the minspan algorithm will definitely select the first one.
            # if we get same min span tree, that means it can be put in min span tree.
            if edges[i][3] not in critical and minspan([edges[i]] + edges, -1, mindist) == mindist:
                others.append(edges[i][3])
        
        return [list(critical), others]


if __name__ == '__main__':
    s = Solution()
    print(s.findCriticalAndPseudoCriticalEdges(n=5,
                                               edges=[[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3],
                                                      [1, 4, 6]]))
    print(s.findCriticalAndPseudoCriticalEdges(n=4, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]))
