# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/6 10:36

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


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n % k != 0:
            return -1

        wc = collections.Counter(nums)
        if any(c > k for c in wc.values()):
            return -1

        if k == n:
            return 0


        def dfs(index, perms, diff, maxdiff):
            if index >= n:
                return sum([max(perm)-min(perm) for perm in perms]) <= maxdiff

            v = nums[index]
            for i in range(k):
                b = not perms[i]
                if v not in perms[i] and len(perms[i]) < n//k:

                    pd = max(perms[i]) - min(perms[i]) if perms[i] else 0
                    perms[i].add(v)
                    d = max(perms[i]) - min(perms[i])
                    if diff + d - pd <= maxdiff:
                        if dfs(index+1, perms, diff + d - pd, maxdiff):
                            return True
                    perms[i].remove(v)
                if b:
                    break

            return False

        INF = sum(nums) + 1
        lo, hi = 0, INF
        while lo <= hi:
            mid = (lo + hi) // 2
            if dfs(0, [set() for _ in range(k)], 0, mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo if lo < INF else -1

if __name__ == '__main__':
    s = Solution()
    print(s.minimumIncompatibility([8,8,9,7,2,7,6,2,7,2], 2))
    print(s.minimumIncompatibility([1, 2, 1, 4], 2))
    print(s.minimumIncompatibility([6,3,8,1,3,1,2,2], 4))
    print(s.minimumIncompatibility([5,3,3,6,3,3], 3))
    print(s.minimumIncompatibility([10,5,6,5,6,3,6,4,2,3], 10))
    print(s.minimumIncompatibility([2,8,2,9,2,8,2,9,6,8,6,8], 6))