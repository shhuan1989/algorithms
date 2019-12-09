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
created by shhuan at 2019/12/8 22:22

"""

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        N = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(N)]
        MOD = 2 ** 32
        def check(m):
            h = 0
            for i in range(m):
                h = (h * 26 + nums[i]) % MOD

            # already seen hashes of strings of length L
            seen = {h}
            # const value to be used often : a**L % modulus
            aL = pow(26, m, MOD)
            for start in range(1, N - m + 1):
                # compute rolling hash in O(1) time
                h = (h * 26 - nums[start - 1] * aL + nums[start + m - 1]) % MOD
                if h in seen:
                    return start
                seen.add(h)
            return -1

        lo, hi = 1, N
        ans = -1
        while lo <= hi:
            m = (lo + hi) // 2
            s = check(m)
            if s >= 0:
                ans = s
                lo = m + 1
            else:
                hi = m - 1

        return S[ans: ans+hi]


s = Solution()
print(s.longestDupSubstring('banana'))
print(s.longestDupSubstring('abcd'))
print(s.longestDupSubstring('aaaaaaaaaa'))
