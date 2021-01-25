# -*- coding:utf-8 -*-

"""
created by shuangquan.huang at 2021/1/21
"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        def gettail(head):
            if not head:
                return None
            h = head
            while h.next:
                h = h.next
            return h
        
        if a == 0:
            h = list1
            for _ in range(b):
                h = h.next
            
            tail = gettail(list2)
            tail.next = h.next
            h.next = None
            return list2
        
        h = list1
        for k in range(a - 1):
            h = h.next
        
        t = h
        for k in range(b - a + 1):
            t = t.next
        
        h.next = list2
        tail = gettail(list2)
        tail.next = t.next
        t.next = None
        
        return list1


def list2arr(lst):
    if not lst:
        return []
    arr = []
    h = lst
    while h:
        arr.append(h.val)
        h = h.next
    return arr


def arr2list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    h = head
    for v in arr[1:]:
        h.next = ListNode(v)
        h = h.next
    return head


if __name__ == '__main__':
    s = Solution()
    list1 = arr2list([0, 1, 2])
    list2 = arr2list([1000000, 1000001, 1000002, 1000003])
    ans = s.mergeInBetween(list1, 1, 1, list2)
    print(list2arr(ans))
