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
created by shhuan at 2019/12/19 16:39

"""

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        g = collections.defaultdict(list)

        for a, b in zip(pid, ppid):
            g[b].append(a)


        def dfs(u):
            ans = [u]
            for v in g[u]:
                ans.extend(dfs(v))

            return ans

        return dfs(kill)

s = Solution()
print(s.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5))