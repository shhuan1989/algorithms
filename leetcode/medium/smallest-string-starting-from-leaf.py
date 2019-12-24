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
created by shhuan at 2019/12/23 19:15

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:


        def dfs(node):
            if not node:
                return ''

            ch = chr(node.val + ord('a'))
            if not node.left and not node.right:
                return ch
            if not node.left:
                return dfs(node.right) + ch
            if not node.right:
                return dfs(node.left) + ch

            left = dfs(node.left)
            right = dfs(node.right)
            return min(left + ch, right + ch)

        return dfs(root)

s = Solution()
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(0)

print(s.smallestFromLeaf(root))