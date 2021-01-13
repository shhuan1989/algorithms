# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/12/1

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


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        
        pre = pHead
        curr = pre.next
        pre.next = None
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        
        return pre
    
    
if __name__ == '__main__':
    s = Solution()
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    print(s.ReverseList(h))