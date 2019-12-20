# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/20/19

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
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        
        ps = collections.defaultdict(list)
        ps[0] = [0]
        h = head
        s = 0
        i = 0
        rem = []
        N = 0
        while h:
            s += h.val
            if s in ps:
                for j in ps[s]:
                    rem.append((j, i))
            i += 1
            ps[s].append(i)
            h = h.next
        N = i
        if not rem:
            return head
        
        rem.sort()
        nrem = [rem[0]]
        for i in range(1, len(rem)):
            if rem[i][1] < nrem[-1][1]:
                continue
            if rem[i][0] > nrem[-1][1]:
                nrem.append(rem[i])
        
        rem = [False for _ in range(N)]
        for l, r in nrem:
            for i in range(l, r+1):
                rem[i] = True
                
        ans = ListNode(0)
        tail = ans
        i, h = 0, head
        while h:
            if not rem[i]:
                tail.next = ListNode(h.val)
                tail = tail.next
            h = h.next
            i += 1
            
        return ans.next



def list2Noode(a):
    if not a:
        return None
    
    h = ListNode(a[0])
    h.next = list2Noode(a[1:])
    return h


def node2List(node):
    ans = []
    h = node
    while h:
        ans.append(h.val)
        h = h.next
    
    return ans
        
s = Solution()
print(node2List(s.removeZeroSumSublists(list2Noode([1,2,-3,3,1]))))
print(node2List(s.removeZeroSumSublists(list2Noode([1,2,3,-3,4]))))
print(node2List(s.removeZeroSumSublists(list2Noode([1,2,3,-3,-2]))))
print(node2List(s.removeZeroSumSublists(list2Noode([1, -1]))))
print(node2List(s.removeZeroSumSublists(list2Noode([1,3,2,-3,-2,5,5,-5,1]))))
