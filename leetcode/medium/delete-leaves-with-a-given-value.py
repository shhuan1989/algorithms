# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/20

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
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        
        def dfs(node):
            if not node:
                return True
            
            if not node.left and not node.right and node.val == target:
                return True
            
            x = dfs(node.left)
            y = dfs(node.right)
            if x:
                node.left = None
            if y:
                node.right = None
            
            return x and y and node.val == target
        
        if dfs(root):
            return None
        
        return root