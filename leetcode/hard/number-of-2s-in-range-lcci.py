# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/10/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        
        a = []
        while n > 0:
            a.append(n % 10)
            n //= 10
        a = a[::-1]
        na = len(a)
        
        
        def ncr(c, r):
            if r > c:
                return 0
            if r == 0 or r == c:
                return 1
            if r > c-r:
                return ncr(c, c-r)
            
            return ncr(c-1, r-1) + ncr(c-1, r)
        
        def dfs(x, two, index, op):
            if index >= na:
                return two if op <= 0 else 0
            
            if op > 0:
                return 0
            elif op == 0:
                ans = 0
                for v in range(a[index]):
                    ans += dfs(x*10 + v, two + (1 if v == 2 else 0), index+1, -1)
                ans += dfs(x*10 + a[index], two + (1 if a[index] == 2 else 0), index+1, 0)
                print(x, ans)
                return ans
            else:
                rest = na-index
                ans = two * 10**rest
                for i in range(1, rest+1):
                    ans += 9**(rest-i) * i * ncr(rest, i)
                print(x, ans)
                return ans
            
        
        return dfs(0, 0, 0, 0)
        

if __name__ == '__main__':
    
    s = Solution()
    print(s.numberOf2sInRange(25))