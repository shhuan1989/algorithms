# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/26

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1, -1)
    
    def add(self, node: ListNode) -> int:
        h = self.head
        while h.next:
            h = h.next
            if h.key == node.key:
                h.val = node.val
                return 0
        h.next = node
        return 1
    
    def remove(self, key: int) -> int:
        h = self.head
        while h.next:
            hn = h.next
            if hn.key == key:
                hnn = hn.next
                hn.next = None
                h.next = hnn
                return 1
            h = hn
        
        return 0
            
    def to_list(self) -> List[ListNode]:
        h = self.head.next
        nodes = []
        while h:
            hn = h.next
            h.next = None
            nodes.append(h)
            h = hn
        return nodes
    
    def find(self, key: int) -> int:
        h = self.head.next
        while h:
            if h.key == key:
                return h.val
            h = h.next
        
        return -1


class MyHashMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 8
        self.data = [LinkedList() for _ in range(self.size)]
        self.count = 0
        self.threhold = 0.5
    
    def get_index(self, key):
        return hash(key) % self.size
    
    def put_impl(self, node: ListNode) -> int:
        index = self.get_index(node.key)
        return self.data[index].add(node)
        
    def expand(self):
        self.size *= 2
        kvs = []
        for head in self.data:
            kvs.extend(head.to_list())
        self.data = [LinkedList() for _ in range(self.size)]
        for node in kvs:
            self.put_impl(node)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        if self.count / self.size > self.threhold:
            self.expand()
        self.count += self.put_impl(ListNode(key, value))
    
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.get_index(key)
        return self.data[index].find(key)
    
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.get_index(key)
        self.count -= self.data[index].remove(key)

# Your MyHashMap object will be instantiated and called as such:
m = MyHashMap()

import random
for i in range(10000):
    key = random.randint(0, 1000)
    val = random.randint(0, 1000000)
    m.put(key, val)
    
    if random.randint(0, 100) > 10:
        print(m.get(random.randint(0, 1000)))
