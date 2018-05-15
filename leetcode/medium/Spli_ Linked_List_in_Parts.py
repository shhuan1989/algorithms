# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/19/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        size = self.listSize(root)
        a = size // k
        b = size - a*k

        ans = []
        c = 1
        part = root
        tail = root
        while tail:
            if c == a + (1 if b > 0 else 0):
                ans.append(part)
                part = tail.next
                tail.next = None
                tail = part
                c = 1
                b -= 1
            else:
                c += 1
                tail = tail.next
        ans += [] * (k-len(ans))
        return ans


    def listSize(self, root):
        node = root
        size = 0
        while node:
            size += 1
            node = node.next

        return size