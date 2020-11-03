# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/2

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


class SummaryRanges:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.segs = []
    
    def addNum(self, val: int) -> None:
        segs = self.segs
        if not segs:
            segs.append([val, val])
        
        i = bisect.bisect_left(segs, [val, float('-inf')])
        
        if i >= len(segs):
            if val > segs[-1][1] + 1:
                segs.append([val, val])
            else:
                segs[-1][1] = max(segs[-1][1], val)
        elif segs[i][0] == val:
            pass
        elif segs[i][0] == val + 1:
            segs[i][0] = val
            if i > 0 and segs[i-1][1] >= val-1:
                segs[i][0] = segs[i-1][0]
                self.segs = segs[:i-1] + segs[i:]
        elif i-1 >= 0 and segs[i-1][1] >= val-1:
            segs[i-1][1] = max(segs[i-1][1], val)
            if segs[i-1][1] >= segs[i][0] - 1:
                segs[i][0] = segs[i-1][0]
                self.segs = self[:i-1] + segs[i:]
        else:
            segs.insert(i, [val, val])
    
    def getIntervals(self) -> List[List[int]]:
        return self.segs


if __name__ == '__main__':
    s = SummaryRanges()
    
    # s.addNum(6)
    # s.addNum(8)
    # s.addNum(7)
    # s.addNum(7)
    # print(s.getIntervals())
    
    for op, param in zip(["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"], [[],[6],[],[6],[],[0],[],[4],[],[8],[],[7],[],[6],[],[4],[],[7],[],[5],[]]):
        if op == 'SummaryRanges':
            s = SummaryRanges()
        elif op == 'addNum':
            s.addNum(param[0])
        else:
            print(s.getIntervals())