# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/26

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        
        
        dp = [0 for _ in range(1 << n)]
        dp[0] = 1
        owner = [[] for _ in range(41)]
        for i, v in enumerate(hats):
            for j in v:
                owner[j].append(i)
        
        for i in range(41):
            ndp = [v for v in dp]
            for j in owner[i]:
                for s in range(1 << n):
                    if s & (1 << j) == 0:
                        ndp[s | (1 << j)] += dp[s]
                        ndp[s | (1 << j)] %= 10 ** 9 + 7
            dp = ndp
        return dp[-1]
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.numberWays([[3,4],[4,5],[5]]))
    # print(s.numberWays([[3,5,1],[3,5]]))
    # print(s.numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
    print(s.numberWays([[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]))
    