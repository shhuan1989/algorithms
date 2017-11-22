# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/8 09:18
    
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def dfs(l, r):
            if l == r:
                return [TreeNode(l)]
            elif l > r:
                return []
            ans = []
            for i in range(l, r + 1):
                lefts = dfs(l, i - 1)
                rights = dfs(i + 1, r)

                if not lefts and not rights:
                    ans.append(TreeNode(i))
                elif not lefts:
                    for right in rights:
                        root = TreeNode(i)
                        root.right = right
                        ans.append(root)
                elif not rights:
                    for left in lefts:
                        root = TreeNode(i)
                        root.left = left
                        ans.append(root)
                else:

                    for left in lefts:
                        for right in rights:
                            root = TreeNode(i)
                            root.left = left
                            root.right = right
                            ans.append(root)
            return ans

        return dfs(1, n)












s = Solution()
s.generateTrees(3)