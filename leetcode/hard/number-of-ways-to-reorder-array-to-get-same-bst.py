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


from functools import lru_cache
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        parent = [-1 for _ in range(n)]
        left = [-1 for _ in range(n)]
        right = [-1 for _ in range(n)]
        
        def insert(u, v):
            if nums[u] > nums[v]:
                if left[u] > 0:
                    insert(left[u], v)
                else:
                    left[u] = v
                    parent[v] = u
            else:
                if right[u] > 0:
                    insert(right[u], v)
                else:
                    right[u] = v
                    parent[v] = u
        
        for i in range(1, n):
            insert(0, i)
        
        q = [0]
        depth = [-1 for _ in range(n)]
        levels = collections.defaultdict(list)
        depth[0] = 1
        maxh = 0
        levels[1].append(0)
        while q:
            nq = []
            for u in q:
                maxh = depth[u]
                if left[u] > 0:
                    nq.append(left[u])
                    depth[left[u]] = depth[u] + 1
                    levels[depth[u] + 1].append(left[u])
                if right[u] > 0:
                    nq.append(right[u])
                    depth[right[u]] = depth[u] + 1
                    levels[depth[u] + 1].append(right[u])
            q = nq

        MOD = 10 ** 9 + 7
        
        pii = [1 for _ in range(1005)]
        for i in range(2, 1005):
            pii[i] = (i * pii[i-1]) % MOD
        
        
        @lru_cache(maxsize=None)
        def mypow(v, p):
            if p == 0:
                return 1
            if p == 0:
                return v % MOD
            
            a = mypow(v, p // 2)
            b = (a * a) % MOD
            if p % 2 == 0:
                return b
            else:
                return (b * v) % MOD
        
        
        @lru_cache(maxsize=None)
        def inv(v):
            return mypow(v, MOD-2)
            
            
        @lru_cache(maxsize=None)
        def ncr(c, r):
            if r > c:
                return 0
            
            if r == 0 or r == c:
                return 1
            
            if r > c - r:
                return ncr(c, c-r)
            
            a = pii[c]
            b = pii[c-r]
            c = pii[r]
            return (a * inv(b) * inv(c)) % MOD
        
        
        count = [1 for _ in range(n)]
        
        dp = [0 for _ in range(n)]
        for h in range(maxh, 0, -1):
            for u in levels[h]:
                dp[u] = 1
                if left[u] > 0 and right[u] > 0:
                    dp[u] = ncr(count[left[u]] + count[right[u]], count[left[u]]) * dp[left[u]] * dp[right[u]] % MOD
                elif left[u] > 0:
                    dp[u] = dp[left[u]]
                elif right[u] > 0:
                    dp[u] = dp[right[u]]
                else:
                    pass
                count[u] = 1
                if left[u] > 0:
                    count[u] += count[left[u]]
                if right[u] > 0:
                    count[u] += count[right[u]]
        
        return dp[0] - 1


if __name__ == '__main__':
    s = Solution()
    print(s.numOfWays([2, 1, 3]))
    print(s.numOfWays([3,4,5,1,2]))
    print(s.numOfWays([1, 2, 3]))
    print(s.numOfWays([3,1,2,5,4,6]))
    print(s.numOfWays([9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]))
    