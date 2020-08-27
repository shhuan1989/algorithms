# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/24

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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        def dfs(node):
            # return minval, maxval, maxsum, treesum
            if not node.left and not node.right:
                return True, node.val, node.val, node.val, node.val
            
            if not node.left:
                v, rmin, rmax, rsum, rtsum = dfs(node.right)
                if not v or rmin <= node.val:
                    return False, float('inf'), float('-inf'), max(rsum, 0), 0
                else:
                    return True, node.val, rmax, max(rtsum + node.val, rsum), rtsum + node.val
            
            if not node.right:
                v, lmin, lmax, lsum, ltsum = dfs(node.left)
                if not v or lmax >= node.val:
                    return False, float('inf'), float('-inf'), max(lsum, 0), 0
                else:
                    return True, lmin, node.val, max(ltsum + node.val, lsum), ltsum + node.val
            
            vr, rmin, rmax, rsum, rtsum = dfs(node.right)
            vl, lmin, lmax, lsum, ltsum = dfs(node.left)
            
            if vl and vr and lmax < node.val < rmin:
                return True, lmin, rmax, max(ltsum + rtsum + node.val, lsum, rsum), ltsum + rtsum + node.val
            
            return False, float('inf'), float('-inf'), max(lsum, rsum, 0), 0
        
        v, a, b, c, d = dfs(root)
        
        return max(c, 0)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(9)
    root.left = TreeNode(2)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(3)
    t = root.left.right.left
    t.left = TreeNode(-5)
    t.left.right = TreeNode(1)
    t.right = TreeNode(4)
    t.right.right = TreeNode(10)
    root.right = TreeNode(3)
    print(s.maxSumBST(root))