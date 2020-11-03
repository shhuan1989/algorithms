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
created by shhuan at 2019/12/4 23:22

"""


# class MyCalendarTwo:
#     def __init__(self):
#         self.calendar = []
#         self.overlaps = []
#
#     def book(self, start, end):
#         for i, j in self.overlaps:
#             if start < j and end > i:
#                 return False
#         for i, j in self.calendar:
#             if start < j and end > i:
#                 self.overlaps.append((max(start, i), min(end, j)))
#         self.calendar.append((start, end))
#         return True
#
# import networkx as nx
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('MacOSX')

class Node:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.left = None
        self.right = None
        self.maxv = count
        self.lazy = 0
        

class SegmentTree():
    def __init__(self, start, end):
        self.root = Node(start, end, 0)
    
    def push(self, node):
        if not node:
            return
        
        node.count += node.lazy
        node.maxv += node.lazy
        
        if node.start < node.end:
            mid = (node.start + node.end) // 2
            if not node.left:
                node.left = Node(node.start, mid, node.count)
            else:
                node.left.lazy += node.lazy
            if not node.right:
                node.right = Node(mid+1, node.end, node.count)
            else:
                node.right.lazy += node.lazy
            
        node.lazy = 0
    
    def insert(self, start, end):
        self.insertimpl(self.root, start, end)
    
    def insertimpl(self, node, start, end):
        if start > end:
            return 0
        
        self.push(node)
        
        if start <= node.start and end >= node.end:
            node.lazy += 1
            return node.maxv + node.lazy
        
        if end < node.start or start > node.end:
            return 0
        
        mid = (node.start + node.end) // 2
        
        a = self.insertimpl(node.left, start, min(end, mid))
        b = self.insertimpl(node.right, max(start, mid+1), end)
        
        c = max(a, b)
        node.maxv = c
        
        return node.maxv

    def getmax(self, start, end):
        return self.getmaximpl(self.root, start, end)
    
    def getmaximpl(self, node, start, end):
        if not node:
            return 0
        self.push(node)
        
        if start <= node.start <= node.end <= end:
            return node.maxv
        
        if end < node.start or start > node.end:
            return 0
        
        if not node.left and not node.right:
            return node.maxv

        mid = (node.start + node.end) // 2
        return max(self.getmaximpl(node.left, start, min(end, mid)), self.getmaximpl(node.right, max(start, mid+1), end))

class MyCalendarTwo:
    def __init__(self):
        self.s = SegmentTree(0, 10**9+7)
    
    def book(self, start: int, end: int) -> bool:
        if self.s.getmax(start, end-1) > 1:
            return False
        
        # print(self.s.getmax(start, end-1))
        
        self.s.insert(start, end-1)
        return True


if __name__ == '__main__':
    s = MyCalendarTwo()
    
    books = [[24, 40], [43, 50], [27, 43], [5, 21], [30, 40], [14, 29], [3, 19], [3, 14], [25, 39], [6, 19]]
    # [(10, 20), (50, 60), (10, 40), (5, 15), (5, 10), (25, 55)]:
    # books = books = [[24, 40], [27, 43]]
    for start, end in books:
        print(s.book(start, end))
        # print(s.s.getmax(30, 35))
        # s.s.print()
        # print([s.s.getmax(i, i) for i in range(30, 35)])