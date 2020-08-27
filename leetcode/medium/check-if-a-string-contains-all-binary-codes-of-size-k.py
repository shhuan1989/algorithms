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
    def hasAllCodes(self, s: str, k: int) -> bool:
        vis = [False for _ in range(1 << k)]
        
        a = int(s[:k], 2)
        s = [int(x) for x in s]
        vis[a] = True
        n = len(s)
        for i in range(k, n):
            a <<= 1
            a |= s[i]
            a &= (1 << k) - 1
            # print(bin(a))
            vis[a] = True
        
        # print(vis)
        return all(vis)
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.hasAllCodes("00110110", 2))
    print(s.hasAllCodes("10010111100001110010", 5))