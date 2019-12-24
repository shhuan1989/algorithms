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
created by shhuan at 2019/12/24 22:31

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node.left and not node.right:
                ans = max(ans, 1)
                return node.val, node.val, 1

            if node.left and node.right:
                left_min, left_max, left_num = dfs(node.left)
                right_min, right_max, right_num = dfs(node.right)
                if left_num != -1 and right_num != -1:
                    if left_max < node.val < right_min:
                        ans = max(ans, left_num + right_num + 1)
                        return left_min, right_max, left_num + right_num + 1

            elif node.left and not node.right:
                left_min, left_max, left_num = dfs(node.left)
                if left_num != -1:
                    if left_max < node.val:
                        ans = max(ans, left_num + 1)
                        return left_min, node.val, left_num + 1
            elif not node.left and node.right:
                right_min, right_max, right_num = dfs(node.right)
                if right_num != -1:
                    if node.val < right_min:
                        ans = max(ans, right_num + 1)
                        return node.val, right_max, right_num + 1

            return -1, -1, -1

        dfs(root)
        return ans


