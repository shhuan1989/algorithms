# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2019/11/17 10:37

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.vals = set()

        def dfs(node, val):
            if node is None:
                return

            node.val = val
            self.vals.add(val)
            if node.left is not None:
                dfs(node.left, 2*val+1)
            if node.right is not None:
                dfs(node.right, 2*val+2)

        dfs(root, 0)


    def find(self, target: int) -> bool:
        return target in self.vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

root = TreeNode(-1)
root.right = TreeNode(-1)
root.right.left = TreeNode(-1)
root.right.left.left = TreeNode(-1)

findElements = FindElements(root)
print(findElements.find(2))
print(findElements.find(3))
print(findElements.find(4))
print(findElements.find(5))