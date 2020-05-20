# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/4/27

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
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return None
            
            if node.val == target.val:
                return node
            
            a = dfs(node.left)
            if a:
                return a
            
            return dfs(node.right)
        
        
        return dfs(cloned)
        