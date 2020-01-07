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
created by shhuan at 2019/12/29 10:32

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1 and not root2:
            return []

        a = []
        q = []
        if root1:
            q.append(root1)
        if root2:
            q.append(root2)

        while q:
            node = q.pop()
            a.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        a.sort()
        return a

