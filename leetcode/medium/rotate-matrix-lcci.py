# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # for row in matrix:
        #     print(row)
        # print()
        n = len(matrix)
        for i in range(n):
            for k in range(n-i*2-1):
                r, c, m = i, i, n-i
                v = matrix[r][c]
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    for j in range(n-i*2-1):
                        r, c = r + dr, c + dc
                        # print(r, c, v)
                        matrix[r][c], v = v, matrix[r][c]
                # break
            # matrix[i][i] = v
        
        # for row in matrix:
        #     print(row)
            


s = Solution()
print(s.rotate([[1]]))
print(s.rotate([[1, 2], [3, 4]]))
print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

matrix = [[row*5+col for col in range(5)] for row in range(5)]
print(s.rotate(matrix))


            