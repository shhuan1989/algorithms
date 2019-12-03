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
created by shhuan at 2019/11/18 00:51

"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if K == 0:
            return [target.val]

        def find_parents(node, target, pre):
            if node == target:
                return pre

            if node.left:
                t = find_parents(node.left, target, pre+[node])
                if t:
                    return t
            if node.right:
                t = find_parents(node.right, target, pre+[node])
                if t:
                    return t
            return []

        parents = find_parents(root, target, [])
        # print([node.val for node in parents])


        def find_child(node, dist, parents):
            if node is None:
                return []

            if node == target or node in parents:
                return []

            if dist == 0:
                return [node.val]
            ans = []
            if node.left:
                ans.extend(find_child(node.left, dist-1, parents))
            if node.right:
                ans.extend(find_child(node.right, dist-1, parents))
            return ans

        ans = find_child(target.left, K-1, parents) + find_child(target.right, K-1, parents)

        oparents = [v for v in parents]
        parents = [(v, K-i-1) for i, v in enumerate(reversed(parents)) if K-i-1 >= 0]
        for node, dist in parents:
            ans.extend(find_child(node, dist, [v for v in oparents if v != node]))
        ans = [v for v in ans if v not in [u[0].val for u in parents]]
        ans += [v.val for v, d in parents if d == 0]

        return ans



        # q = [root]
        # ans = []
        # while q:
        #     node = q[-1]
        #     if node == target:
        #         cq = [(node, K)]
        #         while cq:
        #             node, k = cq.pop()
        #             if k == 0:
        #                 ans.append(node.val)
        #             else:
        #                 if node.left:
        #                     cq.append((node.left, k-1))
        #                 if node.right:
        #                     cq.append((node.right, k-1))
        #
        #         q = list(reversed([(v, K - i - 1) for i, v in enumerate(reversed(q)) if K-i-1 >= 0]))
        #         while q:
        #             node, k = q.pop()
        #             cq = [(node, k)]
        #             while cq:
        #                 node, k = cq.pop()
        #                 if k == 0:
        #                     ans.append(node.val)
        #                 else:
        #                     if node.left and node.left != target:
        #                         cq.append((node.left, k-1))
        #                     if node.right and node.right != target:
        #                         cq.append((node.right, k-1))
        #         break
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        #
        # return ans


# root = TreeNode(3)
# root.left = TreeNode(5)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)
# root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(4)
# root.right = TreeNode(1)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(8)


root = TreeNode(0)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.left.right.right.right = TreeNode(4)

s = Solution()
print(s.distanceK(root, root.left.right.right, 0))