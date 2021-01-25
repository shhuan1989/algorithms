# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/24
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
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        a = [[0 for _ in range(m)] for _ in range(n)]
        a[0][0] = matrix[0][0]
        
        q = []
        for r in range(n):
            for c in range(m):
                a[r][c] = (a[r - 1][c - 1] if r - 1 >= 0 and c - 1 >= 0 else 0) ^ (a[r][c - 1] if c - 1 >= 0 else 0) ^ (
                    a[r - 1][c] if r - 1 >= 0 else 0) ^ matrix[r][c]
                heapq.heappush(q, -a[r][c])
        
        for _ in range(k - 1):
            heapq.heappop(q)
        
        return -q[0]


if __name__ == '__main__':
    s = Solution()
    print(s.kthLargestValue([[5, 2], [1, 6]], 1))
    print(s.kthLargestValue([[5, 2], [1, 6]], 2))
    print(s.kthLargestValue([[5, 2], [1, 6]], 3))
    print(s.kthLargestValue([[5, 2], [1, 6]], 4))
