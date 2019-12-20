# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/18/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 16
        self.size = 0
        self.data = [[] for _ in range(self.capacity)]
        
    def index(self, val):
        return hash(val) % self.capacity
    
    def resize(self):
        self.capacity *= 2
        olddata = self.data
        self.data = [[] for _  in range(self.capacity)]
        
        for u in olddata:
            for v in u:
                self.add(v)
        
    
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        self.size += 1
        i = self.index(key)
        self.data[i].append(key)
        
        if self.size * 4 >= self.capacity * 3:
            self.resize()
            
    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        self.size += 1
        i = self.index(key)
        slot = self.data[i]
        slot.remove(key)
    
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = self.index(key)
        for v in self.data[i]:
            if v == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

s = MyHashSet()
s.add(2)
s.add(3)
s.remove(4)
print(s.contains(4))
s.contains(3)
print(s.contains(2))
print(s.contains(3))