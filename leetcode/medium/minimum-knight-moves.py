# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/19/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        def neighbors(r, c):
            return [(r + 1, c + 2), (r + 1, c - 2), (r - 1, c + 2), (r - 1, c - 2), (r + 2, c - 1), (r + 2, c + 1),
                    (r - 2, c - 1), (r - 2, c + 1)]
        
        if x == 0 and y == 0:
            return 0
        
        q = [(0, 0, 0, 0)]
        dist = collections.defaultdict(int)
        heapq.heapify(q)
        while q:
            a, d, r, c = heapq.heappop(q)
            if r == x and c == y:
                return d
            for nr, nc in neighbors(r, c):
                k = (nr, nc)
                if k not in dist or dist[k] > d + 1:
                    dist[k] = d + 1
                    # ASTART 估计的距离需要加上当前的距离d
                    astar = d + max(abs(x - nr), abs(y - nc)) // 2
                    heapq.heappush(q, (astar, d + 1, nr, nc))
        
        return -1
    
s = Solution()
print(s.minKnightMoves(2, 1))
print(s.minKnightMoves(5, 5))
print(s.minKnightMoves(-84, 170))
print(s.minKnightMoves(270, -21))

t0 = time.time()
print(s.minKnightMoves(0, -300))
print(time.time() - t0)