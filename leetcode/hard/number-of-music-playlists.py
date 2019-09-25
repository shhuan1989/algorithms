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


class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        if N > L:
            return 0
        
        MOD = 10**9+7
        
        def f(n, k, l):
            ans = 1
            for i in range(min(k, l)):
                ans *= n-i
                ans %= MOD
            
            ans *= (n-k) ** (l-k)
            ans %= MOD
            return ans
        
        def ncr(c, r):
            if r > c:
                return 0
            
            r = min(r, c-r)
            if r == 0:
                return 1
            
            ans = 1
            for i in range(r):
                ans *= c-i
            for i in range(1, r+1):
                ans //= i
            return ans
        
        ans = 0
        for i in range(1, N+1):
            x, y = f(i, K, L), ncr(N, N-i)
            ans = (x*y-ans+MOD) % MOD
            
        return ans
    
    
s = Solution()
print(s.numMusicPlaylists(2, 3, 1))
print(s.numMusicPlaylists(3, 3, 1))
print(s.numMusicPlaylists(3, 3, 0))