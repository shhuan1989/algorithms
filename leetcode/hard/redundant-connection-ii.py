# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        ind = [0 for _ in range(n + 1)]
        for u, v in edges:
            ind[v] += 1
        
        def check(root, index):
            g = [[] for _ in range(n + 1)]
            for i in range(n):
                if i == index:
                    continue
                u, v = edges[i]
                g[u].append(v)
            vis = [0 for _ in range(n + 1)]
            vis[root] = 1
            q = collections.deque([root])
            while q:
                u = q.popleft()
                vis[u] = 1
                for v in g[u]:
                    q.append(v)
            
            return sum(vis) == n
        
        root = -1
        for v in range(1, n + 1):
            if ind[v] == 0:
                root = v
                break
        for v in range(n + 1):
            if ind[v] > 1:
                for i in range(n - 1, -1, -1):
                    if edges[i][1] == v:
                        if check(root, i):
                            return edges[i]
        
        # cycle
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            
        
        
        
        def get_cycle(u, path, vis):
            
            for v in g[u]:
                if v in vis:
                    return path[path.index(v):]
                
                c = get_cycle(v, path + [v], vis | {v})
                if c:
                    return c
            
            return None

        if root > 0:
            c = get_cycle(root, [root], {root})
            s = (c[-1], c[0])
            for i in range(n - 1, -1, -1):
                u, v = edges[i]
                if (u, v) == s:
                    return edges[i]
        else:
            rg = [[] for _ in range(n+1)]
            for i, (u, v) in enumerate(edges):
                rg[v].append(i)
            for u in range(1, n+1):
                if ind[u] == 1:
                    vi = rg[u][0]
                    if check(u, vi):
                        return edges[vi]
                    
                    

if __name__ == '__main__':
    s = Solution()
    print(s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))
    print(s.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))
    print(s.findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))