# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        indegree = [0 for _ in range(n)]
        for v in leftChild:
            if v >= 0:
                indegree[v] += 1
        for v in rightChild:
            if v >= 0:
                indegree[v] += 1
            
        # print(indegree)
        if len([i for i in range(n) if indegree[i] == 0]) != 1 or any([v > 1 for v in indegree]):
            return False
        
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                root = i
        
        vis = [False for _ in range(n)]
        
        def dfs(node):
            if node < 0:
                return
            vis[node] = True
            dfs(leftChild[node])
            dfs(rightChild[node])
        
        dfs(root)
        # print(vis)
        return all(vis)
        
        
        
        
    

s = Solution()
print(s.validateBinaryTreeNodes(2, [1,0], [-1,-1]))
print(s.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1]))
print(s.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1]))
