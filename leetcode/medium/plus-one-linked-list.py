# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/22 17:58

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        def dfs(node):
            if not node:
                return 1

            rem = dfs(node.next)
            node.val += rem
            rem = node.val // 10
            node.val %= 10

            return rem
        rem = dfs(head)
        if rem > 0:
            ans = ListNode(rem)
            ans.next = head
            return ans

        return head


def arr2List(arr):
    head = ListNode(arr[0])
    h = head
    for v in arr[1:]:
        h.next = ListNode(v)
        h = h.next
    return head

def list2Arr(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

s = Solution()
print(list2Arr(s.plusOne(arr2List([1, 2, 3, 9]))))
print(list2Arr(s.plusOne(arr2List([1, 2, 3, 4]))))
print(list2Arr(s.plusOne(arr2List([9]))))
print(list2Arr(s.plusOne(arr2List([1]))))