# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/9/19

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
    def __init__(self):
        self.index = 0
        
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        def dfs(node):
            if node is None:
                return True, []
            
            if node.val != voyage[self.index]:
                return False, []
            
            self.index += 1
            
            flip = []
            
            if node.left is None and node.right is None:
                return True, []
            elif node.left is None:
                return dfs(node.right)
            elif node.right is None:
                return dfs(node.left)
            
            if node.left.val == voyage[self.index]:
                a, b = dfs(node.left)
                if not a:
                    return False, []
                else:
                    flip.extend(b)
                
                c, d = dfs(node.right)
                if not c:
                    return False, []
                else:
                    flip.extend(d)
            else:
                if node.right.val != voyage[self.index]:
                    return False, []
                
                flip.append(node.val)
                a, b = dfs(node.right)
                if not a:
                    return False, []
                else:
                    flip.extend(b)
                c, d = dfs(node.left)
                if not c:
                    return False, []
                else:
                    flip.extend(d)
            
            return True, flip
        
        
        self.index = 0
        a, b = dfs(root)
        
        if a:
            return b
        else:
            return [-1]

s = Solution()

t = TreeNode(1)
t.left = TreeNode(2)

print(s.flipMatchVoyage(t, [1, 2]))
print(s.flipMatchVoyage(t, [2, 1]))
print(s.flipMatchVoyage(t, [2, 2]))

t.right = TreeNode(3)
print(s.flipMatchVoyage(t, [1, 2, 3]))
print(s.flipMatchVoyage(t, [1, 3, 2]))