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
created by shhuan at 2019/12/19 23:02

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxVal = 0

    def longestConsecutive(self, root: TreeNode) -> int:


        def longestPath(node):
            if not node:
                return 0, 0

            inr, dcr = 1, 1
            if node.left:
                linr, ldcr = longestPath(node.left)
                if node.val == node.left.val + 1:
                    dcr = ldcr + 1
                elif node.val == node.left.val - 1:
                    inr = linr + 1
            if node.right:
                rinr, rdcr = longestPath(node.right)
                if node.val == node.right.val + 1:
                    dcr = max(dcr, rdcr + 1)
                elif node.val == node.right.val - 1:
                    inr = max(inr, rinr + 1)
            self.maxVal = max(self.maxVal, dcr+inr-1)
            return inr, dcr

        longestPath(root)
        return self.maxVal




