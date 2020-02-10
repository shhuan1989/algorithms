# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/2/20

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
    def maxProduct(self, root: TreeNode) -> int:
        
        def sumall(node):
            if not node:
                return 0
            
            return node.val + sumall(node.left) + sumall(node.right)
        
        
        s = sumall(root)
        
        
        def dfs(node):
            if not node:
                return float('-inf'), 0
            
            
            la, lb = dfs(node.left)
            ra, rb = dfs(node.right)
            
            c = node.val + lb + rb
            d = s - c
            
            return max(la, ra, c * d), c
        
        
        ans, _ = dfs(root)
        
        return ans % (10**9+7)
    
    
s = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
print(s.maxProduct(root))

            

        
        
        
