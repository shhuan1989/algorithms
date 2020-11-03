# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/27

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        
        maxprofit = 0
        minstep = 0
        
        s = 0
        profit, cost = 0, 0
        for i, v in enumerate(customers):
            s += v
            
            on = min(s, 4)
            profit += boardingCost * on
            cost += runningCost
            
            p = profit - cost
            # print(p)
            if p > maxprofit:
                maxprofit = p
                minstep = i + 1
            
            s -= on
        
        step = len(customers)
        while s > 0:
            step += 1
            on = min(s, 4)
            profit += boardingCost * on
            cost += runningCost
            p = profit - cost
            # print(p)
            if p > maxprofit:
                maxprofit = p
                minstep =step

            s -= on
        
        return minstep if maxprofit > 0 else -1
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.minOperationsMaxProfit([8, 3], 5, 6))
    print(s.minOperationsMaxProfit([10, 9, 6], 6, 4))
    print(s.minOperationsMaxProfit([3,4,0,5,1], 1, 92))
    print(s.minOperationsMaxProfit([10,10,6,4,7], 3, 8))
    
            
            