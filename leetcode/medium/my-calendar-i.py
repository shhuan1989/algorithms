# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/2/19

"""

import collections
import time
import os
import sys
import bisect
import heapq


class MyCalendar:
    
    def __init__(self):
        self.books = []
        
    def book(self, start: int, end: int) -> bool:
        if not self.books:
            self.books.append((start, end))
            return True
        
        b = (start, float('-inf'))
        i = bisect.bisect_left(self.books, b)
        
        if i == 0:
            if end > self.books[0][0]:
                return False
            self.books = [(start, end)] + self.books
            return True
        elif i == len(self.books):
            if start < self.books[-1][1]:
                return False
            self.books.append((start, end))
            return True
        else:
            if start <= self.books[i][0] < end or self.books[i-1][0] <= start < self.books[i-1][1]:
                return False
            bisect.insort_left(self.books, (start, end))
            return True
            
        
# [null,true,true,false,false,true,false,true,true,true,false]
cal = MyCalendar()
for s, t in [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]:
    print(cal.book(s, t))