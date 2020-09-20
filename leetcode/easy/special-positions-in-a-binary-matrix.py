# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/13 10:30

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
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows = {i for i in range(n) if sum(mat[i]) == 1}
        cols = {i for i in range(m) if sum([mat[r][i] for r in range(n)]) == 1}
        ans = 0
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1 and r in rows and c in cols:
                    ans += 1

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.numSpecial([
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,0,0],
        [1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,0]]))