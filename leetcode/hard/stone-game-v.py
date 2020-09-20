# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/23 10:56

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


from functools import lru_cache
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:

        N = len(stoneValue)
        S = [[0 for _  in range(N)] for _ in range(N)]

        for l in range(N):
            s = 0
            for r in range(l, N):
                s += stoneValue[r]
                S[l][r] = s


        @lru_cache(maxsize=None)
        def dfs(l, r):
            if l >= r:
                return 0

            if r-l == 1:
                return min(stoneValue[l:r+1])

            s = 0
            ans = 0
            for i in range(l, r):
                s += stoneValue[i]
                if s < S[l][r] - s:
                    ans = max(ans, s + dfs(l, i))
                elif s == S[l][r] - s:
                    ans = max(ans, s + dfs(l, i))
                    ans = max(ans, s + dfs(i+1, r))
                else:
                    ans = max(ans, S[l][r] - s + dfs(i+1, r))

            return ans

        return dfs(0, N-1)


if __name__ == '__main__':
    s = Solution()
    print(s.stoneGameV([98,77,24,49,6,12,2,44,51,96]))
    print(s.stoneGameV([6, 2, 3, 4, 5, 5]))
    print(s.stoneGameV( [7] * 500))
    print(s.stoneGameV([4]))
    print(s.stoneGameV([1, 1, 2]))

    import random
    print(s.stoneGameV([random.randint(0, 10**6)] * 500))