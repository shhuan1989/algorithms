# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        
        N = len(points)
        ans = [0, 1]
        count = 0
        for i in range(N):
            xa, ya = points[i]
            vis = set()
            for j in range(i + 1, N):
                if j in vis:
                    continue
                xb, yb = points[j]
                cc = 0
                for k in range(j+1, N):
                    xc, yc = points[k]
                    if (yc - ya) * (xb - xa) == (yb - ya) * (xc - xa):
                        cc += 1
                        vis.add(k)
                if cc > count:
                    ans = [i, j]
                    count = cc
        
        return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.bestLine([[0,0],[1,1],[1,0],[2,0]]))