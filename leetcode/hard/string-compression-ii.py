# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        N = len(s)
        
        def compress(x):
            pass
        
        
        def dfs(i, j, pos):
            
            for ppos in range(pos):
                pres = dfs(pos, j-1, ppos)
                s = pres
            
            