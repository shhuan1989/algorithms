# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/4/19

这道题可以看做如下过程：在数组 arr 中，每次取相邻的两个数 a 和 b，然后去掉其中较小的一个，花费代价为 a * b，
求最终将数组消减为一个元素的最小代价。
那么，要想获得最小代价，我们应该采取的策略是：对于数组中的某一个数 a，分别向左和向右查询比它大的第一个数，
在这两个数中选择较小的那个数把它消去，花费的代价最小。这个过程我们可以用单调栈来一次遍历解决掉。

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        s = [float('inf')]
        for v in arr:
            while v >= s[-1]:
                ans += s[-1] * min(v, s[-2])
                s.pop()
            s.append(v)
        
        while len(s) > 2:
            ans += s[-1] * s[-2]
            s.pop()
        
        return ans
        
    
s = Solution()
print(s.mctFromLeafValues([6, 2, 4]))
print(s.mctFromLeafValues([11, 12, 12]))