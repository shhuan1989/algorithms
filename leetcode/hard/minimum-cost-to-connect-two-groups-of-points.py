# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/20 10:53

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
    def connectTwoGroups(self, cost: List[List[int]]) -> int:

        ans = [float('inf')]

        n, m = len(cost), len(cost[0])

        def argmin(a):
            minv, mini = float('inf'), -1
            for i, v in enumerate(a):
                if v < minv:
                    minv = v
                    mini = i

            return mini

        mina = [argmin(x) for x in cost]
        minb = [argmin(x) for x in [[cost[r][c] for r in range(n)] for c in range(m)]]



        def dfs(index, vis, pre):
            if index >= n:
                if len(vis) == m:
                    ans[0] = min(ans[0], pre)
                else:
                    for i in range(m):
                        if i not in vis:
                            j = minb[i]
                            pre += cost[j][i]
                    ans[0] = min(ans[0], pre)
                return

            if pre > ans[0]:
                return

            x = [(cost[index][i], i) for i in range(m)]
            x.sort()
            for c, i in x:
                dfs(index+1, vis|{i}, pre+c)

        dfs(0, set(), 0)

        return ans[0]


if __name__ == '__main__':
    s = Solution()
    print(s.connectTwoGroups([[15, 96], [36, 2]]))
    print(s.connectTwoGroups( [[1, 3, 5], [4, 1, 1], [1, 5, 3]]))
    print(s.connectTwoGroups([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]))


