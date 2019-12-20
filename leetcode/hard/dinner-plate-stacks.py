# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/17/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class DinnerPlates:
    
    def __init__(self, capacity: int):
        self.stacks = []
        self.available = []
        self.capacity = capacity
    
    def push(self, val: int) -> None:
        while self.available:
            index = heapq.heappop(self.available)
            if 0 <= index < len(self.stacks):
                s = self.stacks[index]
                s.append(val)
                if len(s) < self.capacity:
                    heapq.heappush(self.available, index)
                return
        
        self.stacks.append([val])
        if self.capacity > 1:
            heapq.heappush(self.available, len(self.stacks)-1)
    
    def pop(self) -> int:
        if not self.stacks:
            return -1
        
        s = self.stacks[-1]
        while not s:
            self.stacks.pop()
            if not self.stacks:
                break
            s = self.stacks[-1]
        if not s:
            return -1
        ans = s.pop()
        
        if not s:
            self.stacks.pop()
        
        return ans
    
    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks):
            return -1
        
        s = self.stacks[index]
        if not s:
            return -1
        
        if len(s) == self.capacity:
            heapq.heappush(self.available, index)
        
        return s.pop()


# dp = DinnerPlates(1)
# for a, b in zip(["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"], [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]):
#     if a == 'DinnerPlates':
#         dp = DinnerPlates(b[0])
#     elif a == 'push':
#         dp.push(b[0])
#     elif a == 'popAtStack':
#         print(dp.popAtStack(b[0]))
#     else:
#         print(dp.pop())
#
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

# ["DinnerPlates","push","push","push","popAtStack","pop","pop"]
# [[1],[1],[2],[3],[1],[],[]]
dp = DinnerPlates(1)
dp.push(1)
dp.push(2)
dp.push(3)
print(dp.popAtStack(1))
print(dp.pop())
print(dp.pop())
