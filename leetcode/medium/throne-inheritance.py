# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dead = set()
        self.child = collections.defaultdict(list)
        self.parent = {}

    def birth(self, parentName: str, childName: str) -> None:
        self.child[parentName].append(childName)
        self.parent[childName] = parentName


    def death(self, name: str) -> None:
        self.dead.add(name)


    def getInheritanceOrder(self) -> List[str]:
        
        currorder = []
        inorder = set()
        def dfs(x):
            if not self.child[x] or all([c in inorder for c in self.child[x]]):
                if x == self.king:
                    return None
                else:
                    y = dfs(self.parent[x])
                    # currorder.append(y)
                    # inorder.add(y)
                    return y
            
            for c in self.child[x]:
                if c not in inorder:
                    # currorder.append(c)
                    # inorder.add(c)
                    return c
        
        curr = self.king
        while curr:
            currorder.append(curr)
            inorder.add(curr)
            curr = dfs(curr)
            
        return [x for x in currorder if x not in self.dead]
        
            
            
            
if __name__ == '__main__':
    s = ThroneInheritance('')
    for op, paran in zip(["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"], [["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [], ["bob"], []]):
        if op == 'ThroneInheritance':
            s = ThroneInheritance(paran[0])
        elif op == 'birth':
            s.birth(paran[0], paran[1])
        elif op == 'getInheritanceOrder':
            print(s.getInheritanceOrder())
        else:
            s.death(paran[0])
    