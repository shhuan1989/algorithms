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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root, o1, o2):
        def dfs(node):
            if not node:
                return None
            if node.val in [o1, o2]:
                return node
        
            left, right = dfs(node.left), dfs(node.right)
            if not left and not right:
                return None
            if left and right:
                return node
            if left:
                return left
            return right
    
        node = dfs(root)
        return node.val if node else -1

if __name__ == '__main__':
    s = Solution()
    A = [3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4]
    root = TreeNode(A[0])
    def dfs(node, index):
        lc = index * 2 + 1
        if lc < len(A) and A[lc] >= 0:
            node.left = TreeNode(A[lc])
            dfs(node.left, lc)
        rc = index * 2 + 2
        if rc < len(A) and A[rc] >= 0:
            node.right = TreeNode(A[rc])
            dfs(node.right, rc)
    
    dfs(root, 0)
    
    print(s.lowestCommonAncestor(root, 5, 1))
