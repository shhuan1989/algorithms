# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/8/25 10:54

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:
            return head

        phead = ListNode(0)
        phead.next = head

        found = True
        while found:
            found = False
            vals = {0: phead}

            node = phead.next
            while node:
                if -node.val in vals:
                    vals[-node.val].next = node.next
                    found = True
                    break
                nvals = {}
                for k, v in vals.items():
                    nvals[k+node.val] = v
                nvals[0] = node
                vals = nvals

                node = node.next

        return phead.next


s = Solution()
head = ListNode(1)
node = head
for v in [2,3,-3,-2]:
    node.next = ListNode(v)
    node = node.next

ans = s.removeZeroSumSublists(head)
node = ans
vals = []
while node:
    vals.append(node.val)
    node = node.next
print(vals)


