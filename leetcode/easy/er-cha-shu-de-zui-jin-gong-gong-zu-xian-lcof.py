# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/12/1

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            if node in [p, q]:
                return node
        
            left, right = dfs(node.left), dfs(node.right)
            if not left and not right:
                return None
            if left and right:
                return node
            if left:
                return left
            return right
    
        return dfs(root)
    
if __name__ == '__main__':
    pass