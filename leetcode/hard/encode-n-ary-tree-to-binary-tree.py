# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/17/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.lastNodes = set()
    
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: Node) -> TreeNode:
        
        
        def dfs(root):
            if not root:
                return None
            
            treeNode = TreeNode(root.val)
            
            if root.children:
                treeNode.left = dfs(root.children[0])
                
                right = treeNode.left
                for node in root.children[1:]:
                    right.right = dfs(node)
                    right = right.right
            
            return treeNode
        
        
        return dfs(root)
        
        
        
    
    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> Node:
        
        def dfs(root):
            if not root:
                return None
            
            node = Node(root.val)
            children = []
            if root.left:
                children.append(dfs(root.left))
                right = root.left.right
                while right:
                    rnode = dfs(right)
                    children.append(rnode)
                    right = right.right
            node.children = children
            
            return node
        
        return dfs(data)
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
codec = Codec()

root = Node(1, [])
root.children = [Node(i+2, []) for i in range(3)]
root.children[1].children = [Node(i+7, []) for i in range(2)]

codec.encode(root)
nroot = codec.decode(codec.encode(root))
print(nroot)
