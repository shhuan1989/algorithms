# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/12 13:00

"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        A = board
        M = len(A)
        N = len(A[0])

        if not A:
            return


        for r in range(M):
            for c in range(N):
                p = 0
                for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0 )]



s = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.left.right = TreeLinkNode(5)
root.left.left = TreeLinkNode(4)
root.left.left.left = TreeLinkNode(7)
root.right = TreeLinkNode(3)
root.right.right = TreeLinkNode(6)
root.right.right.right = TreeLinkNode(8)
s.connect(root)

q = [root]
while q:
    node = q.pop(0)
    if node.left:
        q.append(node.left)
    while node:
        sys.stdout.write('{} -> '.format(node.val))
        node = node.next
    print('')