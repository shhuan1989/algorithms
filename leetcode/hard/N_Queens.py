  # -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 13:56

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
import copy
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        q = [([], 0)]
        for row in range(n):
            nq = []
            for col in range(n):
                for s, c in q:
                    cannot = c & (1 << col) != 0
                    cannot = cannot or any([abs(si - row) == abs(sv - col) for si, sv in enumerate(s)])
                    if not cannot:
                        nq.append((s+[col], c | (1 << col)))
            q = nq

        ans = []
        for s, _ in q:
            ans.append([''.join(['.' if s[r] != c else 'Q' for c in range(n)]) for r in range(n)])
        return ans




s = Solution()
ans = s.solveNQueens(5)
for a in ans:
    print('=' * 40)
    for row in a:
        print(row)

startTime = datetime.datetime.now()
# print(s.solveNQueens(9))
print('Time Cose: {}'.format(datetime.datetime.now() - startTime))
