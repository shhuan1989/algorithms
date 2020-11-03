# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/10/13 20:11

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class Solution:
    def numberOfArrays(self, s: str, K: int) -> int:
        s = [int(x) for x in s]
        if s[0] == 0:
            return 0
        
        for v in s:
            if v > K:
                return 0
        
        n = len(s)
        # pre = [0 for _ in range(n)]
        # for i, v in enumerate(s):
        #     if v != 0:
        #         pre[i] = i
        #     else:
        #         pre[i] = pre[i-1]
        
        l, r = 0, 0
        zeros = 0
        while r < n:
            if s[r] != 0:
                zeros = max(zeros, r - l)
                l = r + 1
            r += 1
        zeros = max(zeros, n - l)
        if zeros > 9:
            return 0
        
        MOD = 10 ** 9 + 7
        
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            
            v = s[i]
            if v > 0:
                dp[i] += dp[i - 1]
            
            k = 1
            for j in range(i - 1, -1, -1):
                k *= 10
                v += k * s[j]
                if v > K:
                    break
                
                if v >= 1 and s[j] != 0:
                    dp[i] += dp[j - 1] if j - 1 >= 0 else 1
                    dp[i] %= MOD
        
        return dp[-1] % MOD



if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArrays('10000', 100))
    print(s.numberOfArrays('1317', 2000))
    print(s.numberOfArrays('2020', 30))
    print(s.numberOfArrays('1234567890', 90))
    print(s.numberOfArrays('1' + '0' * 100000, 233))
