# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/15

https://www.geeksforgeeks.org/treap-set-2-implementation-of-search-insert-and-delete/

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import random

class TreeNode:
    def __init__(self, val, rank):
        self.val = val
        self.rank = rank
        self.left = None
        self.right = None
        

class Treap:
    def __init__(self):
        self.root = None
    
    def build(self, data):
        for v in data:
            self.insert(v)
        
    
    def search(self, x):
        return self.search_impl(self.root, x)
    
    def search_impl(self, root, x):
        if root is None or root.val == x:
            return root
        
        if root.val < x:
            return self.search_impl(root.right, x)
        
        return self.search_impl(root.left, x)
    
    def insert(self, x):
        self.root = self.insert_impl(self.root, x)
    
    def insert_impl(self, root, x):
        if not root:
            return TreeNode(x, random.randint(0, 100))
        
        if x <= root.val:
            root.left = self.insert_impl(root.left, x)
            if root.left.rank > root.rank:
                root = self.right_rotate(root)
        else:
            root.right = self.insert_impl(root.right, x)
            if root.right.rank > root.rank:
                root = self.left_rotate(root)
        return root
        
    def delete(self, x):
        return self.delete_impl(self.root, x)
    
    def delete_impl(self, root, x):
        if not root:
            return root
        
        if x < root.val:
            root.left = self.delete_impl(root.left, x)
        elif x > root.val:
            root.right = self.delete_impl(root.right, x)
        else:
            if not root.left:
                right = root.right
                root.right = None
                root = right
            elif not root.right:
                root = self.right_rotate(root)
                root.right = self.delete_impl(root.right, x)
            else:
                root = self.left_rotate(root)
                root.left = self.delete_impl(root.left, x)
            
        return root
    
    def left_rotate(self, root):
        if root is None:
            return root
        
        right = root.right
        rightleft = right.left
        right.left = root
        root.right = rightleft
        
        return right
    
    def right_rotate(self, root):
        left = root.left
        leftright = left.right
        left.right = root
        root.left = leftright
        
        return left
    
    def print(self):
        # print(' '.join(['({}, {})'.format(node.val, node.rank) for node in self.inorder(self.root)]))
        self.inorder(self.root)
        
    def inorder(self, root):
        if not root:
            return []
        
        a = self.inorder(root.left)
        
        print('{}-{}'.format(root.val, root.rank), end=' ')
        if root.left:
            print('|{}-{}'.format(root.left.val, root.left.rank), end=' ')
        else:
            print('| - ', end=' ')
        if root.right:
            print('|{}-{}|'.format(root.right.val, root.right.rank))
        else:
            print('| - |')
        
        b = self.inorder(root.right)
        
        return a + [root] + b
        
        
if __name__ == '__main__':
    data = [50, 30, 20, 40, 70, 60, 80]
    t = Treap()
    t.build(data)
    
    t.print()