# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) < 2:
            return True
        
        d = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if d != arr[i+1] - arr[i]:
                return False
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.canMakeArithmeticProgression([3, 5, 1]))
    print(s.canMakeArithmeticProgression([1, 2, 4]))