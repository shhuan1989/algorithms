# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/22 10:01

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        n, m = len(grid), len(grid[0])
        
        def getid(row, col, index):
            return row * m * 4 + col * 4 + index
        
        parent = [i for i in range(n * m * 4)]
        
        def find(u):
            pu = parent[u]
            if u == pu:
                return pu
            parent[u] = find(pu)
            
            return parent[u]
        
        def merge(u, v):
            # print('merge {} {}'.format(u, v))
            pu, pv = find(u), find(v)
            parent[pu] = pv
            
        # 3 0
        # 2 1
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '\\':
                    merge(getid(r, c, 0), getid(r, c, 1))
                    merge(getid(r, c, 2), getid(r, c, 3))
                elif grid[r][c] == '/':
                    merge(getid(r, c, 1), getid(r, c, 2))
                    merge(getid(r, c, 0), getid(r, c, 3))
                else:
                    for i in range(1, 4):
                        merge(getid(r, c, 0), getid(r, c, i))
                
                # merge with neighbors
                if c + 1 < m:
                    merge(getid(r, c, 1), getid(r, c + 1, 3))
                if r - 1 >= 0:
                    merge(getid(r, c, 0), getid(r - 1, c, 2))
                if c - 1 >= 0:
                    merge(getid(r, c, 3), getid(r, c - 1, 1))
                if r + 1 < n:
                    merge(getid(r, c, 2), getid(r + 1, c, 0))
        
        return len({find(u) for u in range(n * m * 4)})


if __name__ == '__main__':
    s = Solution()
    print(s.regionsBySlashes([' /', '/ ']))
    print(s.regionsBySlashes([' /', '  ']))
    print(s.regionsBySlashes(['\\/', '/\\']))
    print(s.regionsBySlashes(["/\\", "\\/"]))
    print(s.regionsBySlashes(['//', '/ ']))
