# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/12

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        wc = collections.Counter(inventory)
        wc[0] = 0
        keys = list(sorted(wc.keys(), reverse=True))
        
        ans = 0
        mod = 10 ** 9 + 7
        
        for i in range(len(keys) - 1):
            if orders <= 0:
                break
            k, w = keys[i], keys[i + 1]
            d = k - w
            if wc[k] * d <= orders:
                orders -= wc[k] * d
                
                x = d * (2 * k - d + 1) // 2
                ans += x * wc[k]
                ans %= mod
                
                i += 1
                wc[w] += wc[k]
                wc[k] = 0
            else:
                d = orders // wc[k]
                orders -= wc[k] * d
                x = d * (2 * k - d + 1) // 2
                ans += x * wc[k]
                ans %= mod
                
                ans += orders * (k - d)
                ans %= mod
                orders = 0
        
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([2,8,4,10,6], 20))
    print(s.maxProfit([3, 5], 6))
    print(s.maxProfit([2, 5], 4))
    print(s.maxProfit([1000000000], 1000000000))