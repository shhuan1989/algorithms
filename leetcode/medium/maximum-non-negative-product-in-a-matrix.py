# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/20 10:40

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
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dp = [[[float('-inf'), float('-inf')] for _ in range(m)] for _ in range(n)]
        if grid[0][0] > 0:
            dp[0][0][0] = grid[0][0]
        elif grid[0][0] < 0:
            dp[0][0][1] = -grid[0][0]
        else:
            dp[0][0][0] = 0
            dp[0][0][1] = 0


        for r in range(n):
            for c in range(m):
                if r == 0 and c == 0:
                    continue

                if grid[r][c] > 0:
                    if r-1 >= 0:
                        dp[r][c][0] = max(dp[r][c][0], dp[r-1][c][0] * grid[r][c])
                        dp[r][c][1] = max(dp[r][c][1], dp[r-1][c][1] * grid[r][c])
                    if c-1 >= 0:
                        dp[r][c][0] = max(dp[r][c][0], dp[r][c-1][0] * grid[r][c])
                        dp[r][c][1] = max(dp[r][c][1], dp[r][c - 1][1] * grid[r][c])
                elif grid[r][c] < 0:
                    x = abs(grid[r][c])
                    if r-1 >= 0:
                        dp[r][c][0] = max(dp[r][c][0], dp[r-1][c][1] * x)
                        dp[r][c][1] = max(dp[r][c][1], dp[r-1][c][0] * x)
                    if c-1 >= 0:
                        dp[r][c][0] = max(dp[r][c][0], dp[r][c-1][1] * x)
                        dp[r][c][1] = max(dp[r][c][1], dp[r][c - 1][0] * x)
                else:
                    dp[r][c][0] = max(dp[r][c][0], 0)
                    dp[r][c][1] = max(dp[r][c][1], 0)


        # for row in dp:
        #     print(row)

        return dp[-1][-1][0] % (10 ** 9 + 7) if dp[-1][-1][0] >= 0 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.maxProductPath( [[-1,-2,-3],
             [-2,-3,-3],
             [-3,-3,-2]]))
    print(s.maxProductPath( [[1,-2,1],
             [1,-2,1],
             [3,-4,1]]))
    print(s.maxProductPath( [[1, 3],
             [0,-4]]))
    print(s.maxProductPath( [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]))