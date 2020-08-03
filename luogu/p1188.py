# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/22

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
from typing import Tuple, NoReturn
import random

class TreeNode:
    def __init__(self, key: int, prior: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.key = key
        self.left = left
        self.right = right
        self.prior = prior
        self.count = 1

class Treap:
    def __init__(self):
        self.root = None
    
    def build(self, data: List[int]):
        for v in data:
            self.root = self.insert(self.root, TreeNode(v, random.randint(0, 10**9)))
            
    def split(self, node: TreeNode, key: int) -> Tuple[TreeNode, TreeNode]:
        if not node:
            return node, node
        
        ckey = (node.left.count if node.left else 0) + 1
        if key < ckey:
            l, r = self.split(node.left, key)
            node.left = r
            self.update_count(l)
            self.update_count(node)
            return l, node
        else:
            l, r = self.split(node.right, key-ckey)
            node.right = l
            self.update_count(r)
            self.update_count(node)
            return node, r
        
    def insert(self, root: TreeNode, node: TreeNode) -> TreeNode:
        if not root:
            return node
        
        if root.prior < node.prior:
            l, r = self.split(root, node.key)
            node.left = l
            node.right = r
            self.update_count(node)
            return node
        else:
            if root.key < node.key:
                root.right = self.insert(root.right, node)
            else:
                root.left = self.insert(root.left, node)
            self.update_count(root)
            return root
        
    def merge(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t2 if not t1 else t1
        
        if t1.prior > t2.prior:
            t2.left = self.merge(t1, t2.left)
            self.update_count(t2)
            return t2
        else:
            t1.right = self.merge(t1.right, t2)
            self.update_count(t1)
            return t1
    
    def erase(self, root:TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        if root.key == key:
            node = self.merge(root.left, root.right)
            self.update_count(node)
            return node
            
        if root.key < key:
            root.right = self.erase(root.right, key)
        else:
            root.left = self.erase(root.left, key)
        self.update_count(root)
        return root
    
    def count(self, root: TreeNode) -> int:
        return root.count if root else 0
    
    def update_count(self, root: TreeNode) -> NoReturn:
        if root:
            root.count = 1 + self.count(root.left) + self.count(root.right)
    
    def findk(self, root: TreeNode, k: int) -> TreeNode:
        if not root:
            return root
        
        if root.count < k:
            return None
        
        lc = root.left.count if root.left else 0
        if lc >= k:
            return self.findk(root.left, k)
        elif lc == k-1:
            return root
        else:
            return self.findk(root.right, k-lc-1)
            
    def inorder(self, root: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        
        lc = root.left.count if root.left else 0
        if lc >= k:
            return self.inorder(root.left, k)
        
        return self.inorder(root.left, k) + [root.key] + self.inorder(root.right, k-lc-1)


MAXN = 100005
class Node:
    def __init__(self,  key):
        self.key = key
        self.left = 0
        self.right = 0
        self.prior = random.randint(0, 10**9)
        self.count = 1
        
T = [Node(i) for i in range(MAXN)]


def update(x):
    T[x].count = T[T[x].left].count + T[T[x].right].count + 1


def merge(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return x+y
    
    if T[x].prior < T[y].prior:
        T[x].right = merge(T[x].right, y)
        update(x)
        return x
    else:
        T[y].left = merge(x, T[y].left)
        update(y)
        return y


def split(now, key):
    if now <= 0:
        return 0, 0
    
    if T[T[now].left].count >= key:
        l, r = split(T[now].left, key)
        T[now].left = r
        update(now)
        return l, now
    else:
        l, r = split(T[now].right, key-T[T[now].left].count-1)
        T[now].right = l
        update(now)
        return now, r
    
    
def inorder(node):
    if node <= 0:
        return []
    
    return inorder(T[node].left) + [T[node].key] + inorder(T[node].right)
    
        
    
if __name__ == '__main__':
    # sys.stdin = open('p1188.in', 'r')
    N, K = map(int, input().split())
    # treap = Treap()
    # treap.build([i for i in range(1, N+1)])
    root = 0
    T[0].count = 0
    for i in range(1, N+1):
        root = merge(root, i)
        
    # print(inorder(root))
    for i in range(K):
        a, b, c = map(int, input().split())
        a -= 1
        # l1, r1 = treap.split(treap.root, b)
        # l2, r2 = treap.split(l1, a)
        #
        # d = treap.merge(l2, r1)
        # l3, r3 = treap.split(d, c)
        # treap.root = treap.merge(l3, treap.merge(r2, r3))
        # print(treap.inorder(treap.root))
        # print('='*80)
        # print(root)
        # print([v.count for v in T[:N+1]])
        # print(inorder(root))
        # print(b)
        l1, r1 = split(root, b)
        
        # print(inorder(l1))
        # print(inorder(r1))
        l2, r2 = split(l1, a)
        root = merge(l2, r1)
        # print(inorder(root))
        l3, r3 = split(root, c)
        root = merge(l3, merge(r2, r3))
        # print(inorder(root))
    
    # ans = treap.inorder(treap.root, 10)
    # print('\n'.join(map(str, ans)))

    l, r = split(root, 10)
    for i in range(10):
        l, r = split(l, 1)
        print(T[l].key)
        l = r