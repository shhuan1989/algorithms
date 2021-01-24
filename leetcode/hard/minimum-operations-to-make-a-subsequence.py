# -*- coding: utf-8 -*-

"""
created by shhuan at 2021/1/3 11:16

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
    def minOperations(self, target: List[int], arr: List[int]) -> int:

        vset = set(target)
        arr = [v for v in arr if v in vset]

        vi = collections.defaultdict(list)
        for i, v in enumerate(arr):
            vi[v].append(i)

        n, m = len(target), len(arr)


        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0

            if i == 0:
                return 1

            ans = 1

            for pi in range(i-1, -1, -1):
                for pj in vi[target[pi]]:
                    if pj >=j:
                        break
                    ans = max(ans, 1 + dfs(pi, pj))

            return ans


        ans = 0
        for i in range(n-1, -1, -1):
            for j in vi[target[i]]:
                ans = max(ans, dfs(i, j))

        # print(ans)
        return len(target) - ans





if __name__ == '__main__':
    s = Solution()
    print(s.minOperations([5, 1, 3], [9, 4, 2, 3, 4]))
    print(s.minOperations([6, 4, 8, 1, 3, 2], [4, 7, 6, 2, 3, 8, 6, 1]))
    print(s.minOperations([16,7,20,11,15,13,10,14,6,8], [11,14,15,7,5,5,6,10,11,6]))