# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/26

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
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        
        N, M = len(matrix), len(matrix[0])
        g = collections.defaultdict(set)
        ind = collections.defaultdict(int)
        
        def getindx(r, c):
            return r * M + c
        
        
        parent = [i for i in range(M * N)]
        
        def find(u):
            pu = parent[u]
            if pu == u:
                return pu
            
            pu = find(pu)
            parent[u] = pu
            return pu
        
        def merge(u, v):
            pu, pv = find(u), find(v)
            parent[pu] = pv
        
        def addedge(u, v):
            if v not in g[u]:
                g[u].add(v)
                ind[v] += 1
        
        for r in range(N):
            vc = collections.defaultdict(list)
            for c, v in enumerate(matrix[r]):
                vc[v].append(c)
            
            for cs in vc.values():
                for i in range(len(cs)-1):
                    merge(getindx(r, cs[i]), getindx(r, cs[i+1]))
        
        for c in range(M):
            vr = collections.defaultdict(list)
            for r, v in enumerate([matrix[r][c] for r in range(N)]):
                vr[v].append(r)
            
            for rs in vr.values():
                for i in range(len(rs)-1):
                    merge(getindx(rs[i], c), getindx(rs[i+1], c))
                    
                    
        start = set()
        for r in range(N):
            vc = collections.defaultdict(list)
            for c, v in enumerate(matrix[r]):
                vc[v].append(getindx(r, c))
            vals = list(sorted(vc.keys()))
            for a, b in zip(vals[:-1], vals[1:]):
                start.add(find(vc[a][0]))
                addedge(find(vc[a][0]), find(vc[b][0]))
            
        for c in range(M):
            vr = collections.defaultdict(list)
            for r, v in enumerate([matrix[r][c] for r in range(N)]):
                vr[v].append(getindx(r, c))
            
            vals = list(sorted(vr.keys()))
            for a, b in zip(vals[:-1], vals[1:]):
                start.add(find(vr[a][0]))
                addedge(find(vr[a][0]), find(vr[b][0]))
                
        q = [i for i in start if ind[i] == 0]
        
        if q:
            idforgroup = {}
            sid = 0
            while q:
                sid += 1
                nq = []
                for i in q:
                    idforgroup[i] = sid
                    for j in g[i]:
                        ind[j] -= 1
                        if ind[j] == 0:
                            nq.append(j)
                q = nq
            
            ans = [[0 for _ in range(M)] for _ in range(N)]
            for r in range(N):
                for c in range(M):
                    ans[r][c] = idforgroup[find(getindx(r, c))]
            
            return ans
        else:
            return [[1 for _ in range(M)] for _ in range(N)]


if __name__ == '__main__':
    s = Solution()
    print(s.matrixRankTransform([[1,2],[3,4]]))
    print(s.matrixRankTransform([[7,7],[7,7]]))
    print(s.matrixRankTransform([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))
    print(s.matrixRankTransform([[7,3,6],[1,4,5],[9,8,2]]))
    print(s.matrixRankTransform([
        [-37,-50,-3,44],
        [-37,46,13,-32],
        [47,-42,-3,-40],
        [-17,-22,-39,24]]))
    
    print(s.matrixRankTransform([
        [-37,-26,-47,-40,-13],
        [22,-11,-44,47,-6],
        [-35,8,-45,34,-31],
        [-16,23,-6,-43,-20],
        [47,38,-27,-8,43]]))