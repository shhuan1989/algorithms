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

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    
    def serialize(self, root: Node) -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        
        levels = []
        q = [root]
        while q:
            nq = []
            children = []
            for node in q:
                cs = []
                for c in node.children:
                    cs.append(len(nq))
                    nq.append(c)
                children.append(cs)
            
            s = '+'.join(['-'.join([str(v), ','.join(map(str, c))]) for v, c in zip([node.val for node in q], children)])
            levels.append(s)
            q = nq
        
        ans = '|'.join(levels)
        
        return ans
        

    
    def deserialize(self, data: str) -> Node:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        levels = data.split('|')
        nextLevel = []
        for level in reversed(levels):            
            nodesstr = level.split('+')
            nnextLevel = []
            for nodestr in nodesstr:
                ns = nodestr.split('-')
                val = ns[0]
                children = []
                if len(ns) > 1 and len(ns[1]) > 0:
                    childrenIndex = [int(x) for x in ns[1].split(',')]
                    children = [nextLevel[i] for i in childrenIndex]
                
                node = Node(val, children)
                nnextLevel.append(node)
            nextLevel = nnextLevel
            
        return nextLevel[0]
        


root = Node(1, [])
root.children = [Node(i+2, []) for i in range(3)]
root.children[1].children = [Node(i+7, []) for i in range(2)]


codec = Codec()
print(codec.serialize(root))
codec.deserialize(codec.serialize(root))

codec.serialize(None)