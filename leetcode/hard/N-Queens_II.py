# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-04-29 16:47

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""
__author__ = 'huash06'

import sys
import os
import datetime
import functools
import itertools
import collections
from typing import List
import time

class Solution:
    def totalNQueens(self, n: int) -> int:
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

        return len(q)


s = Solution()


print(s.totalNQueens(5))

startTime = time.time()
print(s.totalNQueens(11))
print('Time Cose: {:.6f}'.format(time.time() - startTime))