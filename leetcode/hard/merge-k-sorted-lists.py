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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        ans = ListNode(0)
        h = ans
        q = []
        for i, node in enumerate(lists):
            q.append((node.val, i, node))
            nextnode = node.next
            node.next = None
            lists[i] = nextnode
        
        heapq.heapify(q)
        while q:
            v, i, node = heapq.heappop(q)
            h.next = node
            h = h.next
            if lists[i]:
                newnode = lists[i]
                nextnode = newnode.next
                newnode.next = None
                lists[i] = nextnode
                heapq.heappush(q, (newnode.val, i, newnode))
        
        return ans.next
    
def list_to_arr(head):
    a = []
    h = head
    while h:
        a.append(h.val)
        h = h.next
    return a
    
s = Solution()
print(list_to_arr())