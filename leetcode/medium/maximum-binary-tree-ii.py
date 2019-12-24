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
created by shhuan at 2019/12/24 22:01

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        def dfs(node, parent):
            if not node:
                newNode = TreeNode(val)
                parent.right = newNode
            elif node.val < val:
                parent.right = TreeNode(val)
                parent.right.left = node
            else:
                dfs(node.right, node)

        dfs(root.right, root)

        return root