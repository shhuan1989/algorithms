# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/18/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from functools import lru_cache

class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j==0)
            ans = dp(i-1, j-1) * (N-j+1)
            ans += dp(i-1, j) * max(j-K, 0)
            return ans % (10**9+7)
        
        return dp(L, N)
        
    
    
s = Solution()
print(s.numMusicPlaylists(2, 3, 1))
print(s.numMusicPlaylists(3, 3, 1))
print(s.numMusicPlaylists(3, 3, 0))