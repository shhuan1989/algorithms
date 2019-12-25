# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/24/19

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
    
    def confusingNumberII(self, N: int) -> int:
        if N < 6:
            return 0
        if N < 9:
            return 1
        elif N < 10:
            return 2
        
        rev = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        @lru_cache(maxsize=None)
        def confuseLen(l, mid=False):
            if l <= 0:
                return 0
            if l == 1:
                return 2
            
            if mid:
                if l % 2 == 1:
                    return 5 ** l - 3 * (5 ** (l//2))
                else:
                    return 5 ** l - 5 ** (l//2)
            else:
                if l % 2 == 1:
                    return 4 * (5 ** (l-1)) - 4 * 3 * (5 ** (l//2-1))
                else:
                    return 4 * (5 ** (l-1)) - 4 * (5 ** (l//2-1))
                
        k, v = 0, N
        while v > 0:
            k += 1
            v //= 10
            
        ans = sum([confuseLen(i) for i in range(k)])
        
        def isConfused(val):
            return int(val) <= N and val != ''.join([rev[x] for x in val[::-1]])

        @lru_cache(maxsize=None)
        def gen3(pre, vlen):
            if vlen <= 0:
                return [pre]
            g = []
            for v in ['0', '1', '8']:
                g.extend(gen3(v, vlen-1))
            return g
            
        
        #count 1000 => 4321
        target = str(N)
        
        def dfs(pre, index):
            if len(pre) > len(target):
                return 0
            
            if len(pre) == len(target):
                return 1 if isConfused(pre) else 0
            
            count = 0
            for v in ['0', '1', '6', '8', '9']:
                if v == target[index]:
                    count += dfs(pre+v, index+1)
                elif v < target[index]:
                    left = index+1
                    if left == len(target):
                        count += 1 if isConfused(pre+v) else 0
                    else:
                        rest = len(target) - left * 2
                        if rest >= 0:
                            # last n digits is sym with the first one
                            count += confuseLen(rest, True)
        
                            # last n digits doesnot sym with the first one
                            count += (5 ** rest) * (5 ** left - 1)
                        else:
                            a = pre + v
                            b = ''.join([rev[x] for x in a[:len(target) - left][::-1]])
                            c = a + b
                            if not isConfused(c):
                                count += 5 ** (len(target) - left) - 1
                            else:
                                count += 5 ** (len(target) - left)
            
            return count
        
        for start in ['1', '6', '8', '9']:
            if start == target[0]:
                ans += dfs(start, 1)
            elif start < target[0]:
                rest = len(target) - 2
                # last digit is sym with the first one
                ans += confuseLen(rest, True)
                
                # last digit doesnot sym with the first one
                ans += 4 * (5 ** (rest))

        
        return ans

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
        
    
    def confusingNumberII_2(self, N: int) -> int:
        
        if N < 6:
            return 0
        if N < 9:
            return 1
        
        rev = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        def isConfused(val):
            return int(val) <= N and val != ''.join([rev[x] for x in val[::-1]])
        
        def dfs(s):
            if int(s) > N:
                return []
            
            ans = [s] if isConfused(s) else []
            for v in ['0', '1', '6', '8', '9']:
                ans.extend(dfs(s + v))
            
            return ans
        
        ans = []
        for i in ['1', '6', '8', '9']:
            ans.extend(dfs(i))
        
        # print(ans)
        print(len([x for x in ans if len(x) < 4]))
        print(len([x for x in ans if len(x) >= 4]))
        return len(ans)

    
s = Solution()

# print(s.confusingNumberII(2000))
print(s.confusingNumberII_2(9950))

# print(s.confusingNumberII(2000), s.confusingNumberII_2(2000))

# print(s.confusingNumberII(610))
# for i in range(100000):
#     if s.confusingNumberII(i) != s.confusingNumberII_2(i):
#         print(i, s.confusingNumberII(i), s.confusingNumberII_2(i))
print('#' * 40)
# print(s.confusingNumberII(20))
# print(s.confusingNumberII_2(20))
#
# print(s.confusingNumberII(100))
# print(s.confusingNumberII_2(100))
# t0 = time.time()
# print(s.confusingNumberII(10**9))
# print(time.time() - t0)
