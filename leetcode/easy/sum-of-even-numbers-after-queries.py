# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s = sum([v for v in A if v % 2 == 0])
        ans = []
        for v, i in queries:
            pd = A[i] % 2 == 0
            A[i] += v
            nd = A[i] % 2 == 0
            if not pd and nd:
                s += A[i]
            elif not nd and pd:
                s -= (A[i] - v)
            elif pd and nd:
                s += v
            else:
                pass
            ans.append(s)
        return ans


s = Solution()
print(s.sumEvenAfterQueries(A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]))