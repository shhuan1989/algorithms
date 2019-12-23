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
created by shhuan at 2019/12/22 17:02

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:

        def dfs(node):
            if not node:
                return 0, 0, 0

            lavg, lsum, lcount = dfs(node.left)
            ravg, rsum, rcount = dfs(node.right)

            sm = lsum + rsum + node.val
            cnt = lcount + rcount + 1
            avg = sm / cnt

            return max(lavg, avg, ravg), sm, cnt

        return dfs(root)[0]

