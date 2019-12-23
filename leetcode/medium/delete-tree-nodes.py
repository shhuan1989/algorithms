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
created by shhuan at 2019/12/22 22:24

"""


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        edges = {x: list() for x in range(nodes)}
        for x, p in enumerate(parent):
            if p != -1:
                edges[p].append(x)

        node_cnt = [1] * nodes

        def dfs(u):
            for v in edges[u]:
                dfs(v)
                value[u] += value[v]
                node_cnt[u] += node_cnt[v]
            if value[u] == 0:
                node_cnt[u] = 0

        dfs(0)
        return node_cnt[0]


s = Solution()
print(s.deleteTreeNodes(nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]))


