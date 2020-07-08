# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/5/29

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def dfs(head):
            h = head
            for i in range(k - 1):
                hn = h.next
                if not hn:
                    return head, h
                h = hn
            
            h = head
            hn = head.next
            head.next = None
            for i in range(k - 1):
                hnn = hn.next
                hn.next = h
                h = hn
                hn = hnn
            if hn:
                nexthead, nextail = dfs(hn)
                head.next = nexthead
                return h, nextail
            else:
                return h, head
        
        h, t = dfs(head)
        return h


def arr_to_list(a):
    head = ListNode(0)
    h = head
    for v in a:
        h.next = ListNode(v)
        h = h.next
    return head.next


def list_to_arr(head):
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a

s = Solution()
print(list_to_arr(s.reverseKGroup(arr_to_list([2, 1, 4, 3, 5]), 1)))

