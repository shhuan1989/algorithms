import math
import os
import random
import re
import sys
from typing import List
import bisect
import collections
import heapq
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import hashlib


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:


        edges = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort()

        parent = [i for i in range(n+1)]

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
            for i in range(n+1):
                parent[i] = i

        def minspan(edges, exclude, maxdist):
            clean()

            dist = 0
            for w, u, v, i in edges:
                if i == exclude:
                    continue
                if merge(u, v):
                    dist += w
                    if dist > maxdist:
                        return dist
            
            return dist
        
        mindist = minspan(edges, -1, float('inf'))
        crucial = set()
        for i in range(len(edges)):
            if minspan(edges, i, mindist) != mindist:
                crucial.add(i)
        
        others = []
        for i in range(len(edges)):
            if edges[i][3] not in crucial and minspan([edges[i]] + edges, -1, mindist) == mindist:
                others.append(edges[i][3])

        
        return [list(crucial), others]

if __name__ == '__main__':
    s = Solution()
    # print(s.findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))
    # print(s.findCriticalAndPseudoCriticalEdges(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]))
    print(s.findCriticalAndPseudoCriticalEdges(6, [[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]]))