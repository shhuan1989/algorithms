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
created by shhuan at 2020/7/19 13:07

"""


from functools import lru_cache
class Solution:
    def closestToTarget(self, A: List[int], target: int) -> int:
        ans = abs(A[0] - target)
        pre = {A[0]}
        for v in A:
            pre = {u & v for u in pre} | {v}
            ans = min(ans, min([abs(u-target) for u in pre]))

        return ans


    def closestToTarget_binary_search_tle(self, A: List[int], target: int) -> int:
        N = len(A)

        # def getval(l, r):
        #     w = (1 << 32) - 1
        #     for i in range(l, r+1):
        #         w &= A[i]
        #
        #     return w
        M = 1
        while 2 ** M <= N:
            M += 1

        dp = [[0 for _ in range(M)] for _ in range(N)]

        for i in range(N):
            dp[i][0] = A[i]

        for i in range(N):
            for k in range(1, M):
                if i + 2**k > N:
                    break
                dp[i][k] = dp[i][k-1] & dp[i+(1 << (k-1))][k-1]


        def getval(l, r):
            k = 0
            d = r-l+1
            while 2 ** k <= d:
                k += 1
            k -= 1

            if 2 ** k == d:
                return dp[l][k]

            return dp[l][k] & getval(l+2**k, r)

        def search(start):
            ans = 10**9
            lo, hi = 1, N-start
            while lo <= hi:
                m = (lo + hi) // 2
                v = getval(start, start + m - 1)
                ans = min(ans, abs(v - target))
                if v > target:
                    lo = m + 1
                else:
                    hi = m - 1

            return ans

        return min([search(i) for i in range(N)])


    def closestToTarget_dp(self, A: List[int], target: int) -> int:

        def bitset(val, index):
            return val & (1 << index) > 0

        def setbit(val, index):
            return val | (1 << index)

        def getones(index, start, end):
            l, r = start, start
            ones = []
            while r <= end:
                if not bitset(A[r], index):
                    if r > l:
                        ones.append((l, r - 1))
                    l = r + 1
                r += 1
            if r > l:
                ones.append((l, r - 1))

            return ones

        INF = 10 ** 9 + 7
        # op == 0 equal
        # op < 0 less
        # op > 0 greater
        @lru_cache(maxsize=None)
        def dfs(index, state, start, end, op):
            if start > end:
                return INF

            if index < 0:
                return abs(state - target)

            if start == end:
                return abs(A[start] - target)

            if op > 0:
                rest = (1 << (index + 1)) - 1
                for i in range(start, end+1):
                    rest &= A[i]
                state |= rest

                return abs(state - target)

            ans = INF
            cv = bitset(target, index)
            ones = getones(index, start, end)
            nstate = setbit(state, index)
            if op == 0:
                # set current bit to one
                ans = min(ans, min([dfs(index - 1, nstate, l, r, 0 if cv else 1) for l, r in ones] or [INF]))

                # if current bit of some value is 0
                if any([not bitset(A[i], index) for i in range(start, end + 1)]):
                    # bitwise and of all value in A  == 0
                    ans = min(ans, dfs(index - 1, state, start, end, -1 if cv else 0))

            elif op < 0:
                # always choose 1 for current bit
                ans = min(ans, min([dfs(index - 1, nstate, l, r, -1) for l, r in ones] or [INF]))
                if not ones:
                    ans = min(ans, dfs(index - 1, state, start, end, -1))

            return ans

        ans = dfs(31, 0, 0, len(A) - 1, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.closestToTarget([70, 15, 21, 96], 4))
    print(s.closestToTarget([9, 12, 3, 78, 15], 5))
    print(s.closestToTarget([1000000,1000000,1000000], 1))
    print(s.closestToTarget([1, 2, 4, 8, 16], 0))

    import numpy as np
    a = np.loadtxt('./input/5467.npy').astype('int32').tolist()
    t = 343891
    t0 = time.time()
    s.closestToTarget(a, t)
    print(time.time() - t0)

    t0 = time.time()
    s.closestToTarget_dp(a, t)
    print(time.time() - t0)
