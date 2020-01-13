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
created by shhuan at 2020/1/11 22:44

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grand):
            if not node:
                return 0

            ans = node.val if grand else 0
            even = node.val % 2 == 0
            if node.left:
                ans += dfs(node.left, even, parent)
            if node.right:
                ans += dfs(node.right, even, parent)

            return ans

        return dfs(root, False, False)

