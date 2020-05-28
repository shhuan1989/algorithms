# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/26

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(node, isroot, parent, isLeft):
            if not node:
                return []

            left, right = node.left, node.right
            if node.val in to_delete:
                node.left = None
                node.right = None
                if parent:
                    if isLeft:
                        parent.left = None
                    else:
                        parent.right = None
                        
                return dfs(left, True, node, True) + dfs(right, True, node, False)
            else:
                return ([node] if isroot else []) + dfs(left, False, node, True) + dfs(right, False, node, False)
            
        return dfs(root, True, None, False)
        
        
        
            
            
            
        
        