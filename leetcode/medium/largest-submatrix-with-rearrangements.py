# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/19
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
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        ans = 0
        for r in range(n):
            for c in range(m):
                matrix[r][c] = 0 if matrix[r][c] == 0 else (matrix[r-1][c] + 1 if r-1 >= 0 else matrix[r][c])
            sh = list(sorted(matrix[r], reverse=True))
            ans = max(ans, max((w+1)*sh[w] for w in range(m)))
        
        return ans

    
if __name__ == '__main__':
    s = Solution()
    print(s.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
    print(s.largestSubmatrix([[1,0,1,0,1]]))
    print(s.largestSubmatrix([[1,1,0],[1,0,1]]))
    print(s.largestSubmatrix([[0,0],[0,0]]))
    print(s.largestSubmatrix([[1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1],[1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1],[1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0]]))
    