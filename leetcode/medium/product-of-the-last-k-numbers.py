# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/16/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class ProductOfNumbers:
    
    def __init__(self):
        
        self.data = [1]
        self.zeros = []
        
    
    def add(self, num: int) -> None:
        if num == 0:
            self.data.append(self.data[-1])
            self.zeros.append(len(self.data)-1)
        else:
            self.data.append(self.data[-1] * num)
    
    def getProduct(self, k: int) -> int:
        if self.zeros and self.zeros[-1] >= len(self.data) - k:
            return 0
        
        return self.data[-1] // self.data[len(self.data) - k - 1]
        
        
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


s = ProductOfNumbers()
s.add(3)
s.add(0)
s.add(2)
s.add(5)
s.add(4)
print(s.getProduct(2))
print(s.getProduct(3))
print(s.getProduct(4))
s.add(8)
print(s.getProduct(2))