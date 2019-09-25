# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/20/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        x = [float(v) for v in count]
        wc = collections.Counter(x)
        wcl = [(v, k) for k, v in wc.items()]
        wcl.sort(reverse=True)
        mode = wcl[0][1]
        N = len(x)
        x.sort()
        median = x[N//2] if N % 2 != 0 else (x[N//2] + x[N//2+1]) / 2
        
        return [min(x), max(x), sum(x) / N,  median, mode]
    

