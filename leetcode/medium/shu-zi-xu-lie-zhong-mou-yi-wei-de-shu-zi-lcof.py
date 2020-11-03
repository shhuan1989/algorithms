# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/19/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def findNthDigit(self, n: int) -> int:
        
        def getdigits(v):
            w = 0
            while v > 0:
                w += 1
                v //= 10
            return w
        
        def get(index, val, target, op):
            if index >= len(target):
                return 1 if op == 0 else 0
            
            if op < 0:
                return 10 ** (len(target) - index)
            elif op == 0:
                ans = get(index + 1, target[index], target, 0)
                if index > 0:
                    ans += target[index] * 10 ** (len(target) - index - 1)
                else:
                    ans += (target[index] - 1) * 10 ** (len(target) - index - 1)
                return ans
            else:
                return 0
        
        def getwidth(v):
            d = getdigits(v)
            if d == 1:
                return v + 1
            w = 1
            count = 1
            while w < d:
                count += w * (10 ** w - 10 ** (w - 1))
                w += 1
            
            count += d * get(0, 0, [int(x) for x in str(v)], 0)
            
            return count
        
        def brutal(v):
            s = ''.join(map(str, [i for i in range(v+1)]))
            print(s)
            return len(s)
        
        # print(getwidth(8), brutal(8))
        # print(getwidth(12), brutal(12))
        # print(getwidth(88), brutal(88))
        # print(getwidth(101), brutal(101))
        
        lo, hi = 0, n + 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if getwidth(mid) > n:
                hi = mid - 1
            else:
                lo = mid + 1
        
        n -= getwidth(hi)
        
        return int(str(lo)[n])

    
if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(11))
    print(s.findNthDigit(3))
    print(s.findNthDigit(123424224))