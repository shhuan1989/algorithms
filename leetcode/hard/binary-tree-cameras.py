# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/22

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        
        index = [0]
        
        def setindex(node):
            if not node:
                return
            
            index[0] += 1
            node.val = index[0]
            setindex(node.left)
            setindex(node.right)
        
        setindex(root)
        
        
        memo = {}
        
        def dfs(node, val, pval):
            if not node:
                return 0
        
            key = (node.val, val, pval)
            if key in memo:
                return memo[key]
                
            if val == 0 and pval == 0:
                if not node.left and not node.right:
                    return float('inf')
                
                ans = float('inf')
                if node.left and node.right:
                    for a, b in [(0, 1), (1, 0), (1, 1)]:
                        ans = min(ans, dfs(node.left, a, val) + dfs(node.right, b, val))
                elif node.left:
                    ans = min(ans, dfs(node.left, 1, val))
                else:
                    ans = min(ans, dfs(node.right, 1, val))
                
                memo[key] = ans
                return ans
            else:
                a = min(dfs(node.left, 0, val), dfs(node.left, 1, val))
                b = min(dfs(node.right, 0, val), dfs(node.right, 1, val))
                
                ans = a + b + val
                memo[key] = ans
                return ans
            
        
        # print(dfs(root, 0, 0))
        # print(dfs(root, 1, 0))
        return min(dfs(root, 0, 0), dfs(root, 1, 0))
        

if __name__ == '__main__':
    
    s = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(3)
    root.left.left.left.right = TreeNode(3)
    print(s.minCameraCover(root))



    