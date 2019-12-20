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
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        x, y = start
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(x, y, d) for d in range(4)]
        N, M = len(maze), len(maze[0])
        vis = collections.defaultdict(bool)
        for x, y, d in q:
            vis[x, y, d] = True
            
        while q:
            nq = []
            for x, y, d in q:
                dx, dy = dxy[d]
                nx, ny = x + dx, y + dy
                
                if nx < 0 or nx >= N or ny < 0 or ny >= M or maze[nx][ny] == 1:
                    if x == destination[0] and y == destination[1]:
                        return True
                    for d in range(4):
                        if not vis[x, y, d]:
                            vis[x, y, d] = True
                            q.append((x, y, d))
                else:
                    if not vis[nx, ny, d]:
                        vis[nx, ny, d] = True
                        nq.append((nx, ny, d))
            q = nq
                    
        return False
            
s = Solution()
print(s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]))
print(s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2]))