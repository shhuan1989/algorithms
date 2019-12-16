# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/12/19

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
    def maxLevelSum(self, root: TreeNode) -> int:
        
        q = [root]
        ans, maxsum, level = 0, 0, 1
        
        while q:
            nq = []
            s = sum([node.val for node in q])
            if s > maxsum:
                maxsum = s
                ans = level
                
            for node in q:
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            
            level += 1
            q = nq
            
        return ans