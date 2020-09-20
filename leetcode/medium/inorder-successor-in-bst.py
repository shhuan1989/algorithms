# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/9/17 09:43

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


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return False, None

            if node.val > p:
                a, b = dfs(node.left)
                if a:
                    return a, b

                return True, node

            a, b = dfs(node.right)
            return a, b

        a, b = dfs(root)
        return b

if __name__ == '__main__':

    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(s.inorderSuccessor(root, 1))