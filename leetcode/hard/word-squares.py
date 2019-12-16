# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/15 22:19

"""

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        pres = collections.defaultdict(list)
        for w in words:
            for i in range(1, len(w)+1):
                pres[w[:i]].append(w)

        def dfs(square, si):
            if si >= len(square):
                return [[''.join(row) for row in square]]

            pre = ''.join(square[si])
            ws = pres[pre]

            ans = []
            for w in ws:
                ns = square.copy()
                ns[si] = list(w)
                for c in range(si, len(square)):
                    ns[c][si] = w[c]
                    ns[si][c] = w[c]

                ans.extend(dfs(ns, si+1))

            return ans

        ans = []
        for w in words:
            n = len(w)
            square = [['' for _ in range(n)] for _ in range(n)]
            square[0] = list(w)
            for i in range(1, len(w)):
                square[i][0] = w[i]

            ans.extend(dfs(square, 1))

        # for a in ans:
        #     for row in a:
        #         print(row)
        #     print('=' * 30)
        return ans


s = Solution()
print(s.wordSquares(["area","lead","wall","lady","ball"]))