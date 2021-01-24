# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/13 10:33

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
sys.setrecursionlimit(10000)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:

        presum = [0]

        for v in stones:
            presum.append(presum[-1] + v)

        n = len(stones)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for k in range(1, n):
            for i in range(n):
                if i + k >= n:
                    break

                s = presum[i+k+1] - presum[i]
                dp[i][i + k] = s - min(stones[i] + dp[i+1][i+k], stones[i+k] + dp[i][i+k-1])

        return dp[0][n-1]

        # @lru_cache(maxsize=None)
        # def dfs(start, end):
        #     if start >= end:
        #         return 0
        #
        #     s = presum[end+1] - presum[start]
        #     # print(start, end, max(s - stones[start] - dfs(start+1, end), s - stones[end] - dfs(start, end-1)))
        #     return max(s - stones[start] - dfs(start+1, end), s - stones[end] - dfs(start, end-1))
        #
        # return dfs(0, len(stones)-1)


if __name__ == '__main__':
    s = Solution()
    print(s.stoneGameVII([5,3,1,4,2]))
    print(s.stoneGameVII([7,90,5,1,100,10,10,2]))

    import time
    import random
    t0 = time.time()
    a = [random.randint(0, 100) for _ in range(1000)]
    print(s.stoneGameVII(a))
    print(time.time() - t0)