# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/27 19:18

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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []
        node = root
        while node:
            if not node.left:
                ans.append(node.val)
                node = node.right
            else:
                left = node.left
                while left.right and left.right != node:
                    left = left.right
                if left.right is None:
                    left.right = node
                    ans.append(node.val)
                    node = node.left
                else:
                    node = node.right
                    left.right = None
        return ans


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(1)
    print(s.preorderTraversal(root))



