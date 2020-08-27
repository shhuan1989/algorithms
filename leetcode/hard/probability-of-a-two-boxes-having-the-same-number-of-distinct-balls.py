# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/24

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List




fact = [1 for _ in range(55)]
for i in range(2, 55):
    fact[i] = i * fact[i-1]


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        
        n = len(balls)
        m = sum(balls) // 2
        def dfs(index, sa, sb, ca, pa, pb):
            if index >= n:
                return fact[ca] * fact[ca] // pa // pb if sa == sb and ca == m else 0
            
            if abs(sa-sb) > n-index:
                return 0
            
            if ca == m:
                sb += n-index
                if sa == sb:
                    c = fact[m] * fact[m] // pa // pb
                    for i in range(index, n):
                        c //= fact[balls[i]]
                    return c
                else:
                    return 0
            
            c = 0
            for i in range(balls[index]+1):
                c += dfs(index+1, sa + (1 if i > 0 else 0), sb + (1 if i < balls[index] else 0), ca + i, pa * fact[i], pb * fact[balls[index]-i])
                
            return c
        
        # print(dfs(0, 0, 0, 0, 0))
        
        t = fact[m * 2]
        for v in balls:
            t //= fact[v]

        return dfs(0, 0, 0, 0, 1, 1) / t
        
        
        
    

if __name__ == '__main__':
    s = Solution()
    print(s.getProbability([1, 1]))
    print(s.getProbability([2, 1, 1]))
    print(s.getProbability([1, 2, 1, 2]))
    print(s.getProbability([3, 2, 1]))
    print(s.getProbability([6,6,6,6,6,6]))
    