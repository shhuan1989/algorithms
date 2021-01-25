# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/25
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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        if not head or not root:
            return False
        
        def dfs(tnode, lnode):
            if not tnode and not lnode:
                return True
            if not tnode or not lnode:
                return False
            
            if tnode.val != lnode.val:
                return False
            
            return dfs(tnode.left, lnode.next) or dfs(tnode.right, lnode.right)
        
        def search(node):
            if not node:
                return False
            
            if node.val == head.val and dfs(node, head):
                return True
            
            return search(node.left) or search(node.right)
        
        return search(root)


if __name__ == '__main__':
    s = Solution()
