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
created by shhuan at 2019/12/6 23:11

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        xnodes = collections.defaultdict(set)

        def dfs(node, x, y):
            if not node:
                return
            xnodes[x].add((-y, node.val))

            dfs(node.left, x - 1, y - 1)
            dfs(node.right, x + 1, y - 1)

        dfs(root, 0, 0)
        ans = []
        for x in sorted(xnodes.keys()):
            ans.append([v for y, v in xnodes[x]])

        return ans
