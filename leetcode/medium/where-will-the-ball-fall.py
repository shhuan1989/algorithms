# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/27 10:48

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        ans = []
        for c in range(m):
            y = c
            for x in range(n):
                if grid[x][y] == 1:
                    if y + 1 >= m or grid[x][y+1] == -1:
                        y = -1
                        break
                    else:
                        y += 1
                else:
                    if y - 1 < 0 or grid[x][y-1] == 1:
                        y = -1
                        break
                    y -= 1
            ans.append(y)

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
    print(s.findBall([[-1]]))