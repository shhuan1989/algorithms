# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dist = abs(locations[start] - locations[finish])
        if dist > fuel:
            return 0

        n = len(locations)

        locindex = [(v, i) for i, v in enumerate(locations)]
        locindex.sort()

        locloc = {v[0]: i for i, v in enumerate(locindex)}

        dp = [[0 for _ in range(fuel + 1)] for _ in range(n)]
        dp[start][fuel] = 1

        mod = 10 ** 9 + 7

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(curLocIndex, restFuel):
            # print(curLocIndex, restFuel)
            if curLocIndex == start and restFuel == fuel:
                return 1

            if restFuel > fuel:
                return 0

            ans = 0
            loc = locations[curLocIndex]
            loci = locloc[loc]
            for i in range(loci + 1, n):
                destloc, destindex = locindex[i]
                d = abs(destloc - loc)
                if d + restFuel > fuel:
                    break
                ans += dfs(destindex, restFuel + d)
                ans %= mod
            for i in range(loci-1, -1, -1):
                destloc, destindex = locindex[i]
                d = abs(destloc - loc)
                if d + restFuel > fuel:
                    break
                ans += dfs(destindex, restFuel + d)
                ans %= mod

            return ans

        ans = 0
        for i in range(fuel + 1):
            ans += dfs(finish, i)
            ans %= mod

        return ans


    def countRoutes_dp(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0 for _ in range(fuel + 1)] for _ in range(n)]
        dp[start][0] = 1
        MOD = 10 ** 9 + 7
        
        for k in range(fuel+1):
            for i in range(n):
                for j in range(n):
                    d = abs(locations[i] - locations[j])
                    nk = k + d
                    if i != j and nk <= fuel:
                        dp[j][nk] += dp[i][k]
                        dp[j][nk] %= MOD
        
        # for row in dp:
        #     print(row)
        return sum(dp[finish]) % MOD

    
if __name__ == '__main__':
    s = Solution()
    print(s.countRoutes([15,17,12,8,18], 4, 1, 1))
    # print(s.countRoutes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5))
    # print(s.countRoutes(locations = [4,3,1], start = 1, finish = 0, fuel = 6))
    # print(s.countRoutes(locations = [5,2,1], start = 0, finish = 2, fuel = 3))
    # print(s.countRoutes(locations = [2,1,5], start = 0, finish = 0, fuel = 3))
    # print(s.countRoutes(locations = [1,2,3], start = 0, finish = 2, fuel = 40))