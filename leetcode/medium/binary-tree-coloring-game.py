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
created by shhuan at 2019/12/18 22:42

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:

        q = [root]
        target = None
        while q:
            node = q.pop()
            if node.val == x:
                target = node
                break
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        def count(node):
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)

        left, right = count(node.left), count(node.right)
        up = n - left - right - 1
        k = max(left, right, up)

        return n - k < k