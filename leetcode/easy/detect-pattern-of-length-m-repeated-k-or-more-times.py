# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        for i in range(len(arr)):
            s = arr[i: i+m]
            find = True
            for j in range(i+m, i+m*k, m):
                if arr[j: j+m]!= s:
                    find = False
                    break
            if find:
                return True
        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.containsPattern([1,2,4,4,4,4], m = 1, k = 3))
    print(s.containsPattern(arr = [1,2,1,2,1,1,1,3], m = 2, k = 2))
    print(s.containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3))
    print(s.containsPattern(arr = [1,2,3,1,2], m = 2, k = 2))
    print(s.containsPattern(arr = [2,2,2,2], m = 2, k = 3))