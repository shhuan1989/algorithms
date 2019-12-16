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
created by shhuan at 2019/12/15 13:54

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # 解法3:非递归方法
        if not root:
            return
        DONE = 1  # 已读结点
        UNDO = 0  # 未读结点
        res = []
        stack = [(root, UNDO)]
        while stack:
            node, status = stack.pop()
            if not node:
                continue
            if status == UNDO:
                stack.append((node.right, UNDO))
                stack.append((node, DONE))
                stack.append((node.left, UNDO))
            elif status == DONE:
                if k > len(res):
                    res.append(node.val)
                elif abs(res[0] - target) > abs(node.val - target):
                    res.pop(0)
                    res.append(node.val)
        return res

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

s = Solution()
# print(s.closestKValues(root, 3.7, 2))

root = TreeNode(2)
root.left = TreeNode(1)
print(s.closestKValues(root, 4.1, 2))