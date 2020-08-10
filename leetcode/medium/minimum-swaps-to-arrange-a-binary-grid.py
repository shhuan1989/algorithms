# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/2 10:43

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
    def minSwaps(self, grid: List[List[int]]) -> int:

        a = []
        n, m = len(grid), len(grid[0])
        for r, row in enumerate(grid):
            c = 0
            for i in range(m-1, -1, -1):
                if row[i] != 0:
                    break
                c += 1
            a.append(c)


        now = [i for i in range(n)]
        k = m-1
        ans = 0
        # ni = 0
        for ni in range(n):
            sc, sr = -1, -1
            for r, c in enumerate(a):
                if c >= k:
                    sc, sr = c, r
                    break

            if sr < 0:
                return -1

            ans += sr
            a = a[:sr] + a[sr+1:]

            k -= 1



        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minSwaps([[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]))
    print(s.minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]]))
    print(s.minSwaps(grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
    print(s.minSwaps(grid = [[1,0,0],[1,1,0],[1,1,1]]))



