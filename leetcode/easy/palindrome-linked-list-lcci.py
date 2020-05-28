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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        def to_list(node):
            l = []
            while node:
                l.append(node.val)
                node = node.next
            return l
        
        a = to_list(head)
        for i in range(len(a)//2):
            if a[i] != a[len(a)-i-1]:
                return False
            
        return True