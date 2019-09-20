import math
import os
import random
import re
import sys

from typing import List
import bisect

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None

        if len(pre) == 1:
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        i = post.index(pre[1])

        root.left = self.constructFromPrePost(pre[1: i + 2], post[:i+1])
        root.right = self.constructFromPrePost(pre[i + 2:], post[i+1: -1])

        return root


s = Solution()
print(s.constructFromPrePost(pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]))