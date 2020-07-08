# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/2

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

class Solution:
    def nearestPalindromic(self, start: str) -> str:
        
        n = len(start)
        if n == 1:
            return str(int(start) - 1) if int(start) - 1 >= 0 else str(int(start) + 1)
        
        
        def comp(end, diff, pend):
            if end == start:
                return diff, pend
            d = abs(int(start) - int(end))
            if d < diff:
                return d, end
            elif d > diff:
                return diff, pend
            elif d == diff:
                if int(end) < int(pend):
                    return d, end
            
            return diff, pend
            
        
        ans = ''
        mindiff = float('inf')
        if n > 1:
            end = '9' * (n-1)
            mindiff = abs(int(end)-int(start))
            ans = end
            
        end = '1' + '0' * (n-1) +'1'
        mindiff, ans = comp(end, mindiff, ans)
        
        if n % 2 == 0:
            mid = n // 2
    
            end = start[:mid] + start[:mid][::-1]
            mindiff, ans = comp(end, mindiff, ans)
            
            mv = int(start[mid])
            for v in [mv-1, mv+1]:
                if 0 <= v < 10:
                    end = start[:mid-1] + str(v) + str(v) +  start[:mid-1][::-1]
                    mindiff, ans = comp(end, mindiff, ans)
    
            for i in range(mid, n):
                j = 2 * mid - i - 1
                # increase
                for k in range(j, -1, -1):
                    if int(start[k]) < 9:
                        newend = start[:k] + str(int(start[k]) + 1)
                        newend += '0' * (n // 2 - len(newend))
                        newend += newend[::-1]
                        mindiff, ans = comp(newend, mindiff, ans)
                        break
                # decrease
                for k in range(j, mid):
                    if (k > 0 and int(start[k]) > 0) or (k == 0 and int(start[k]) > 1):
                        newend = start[:k] + str(int(start[k]) - 1)
                        newend += '9' * (n // 2 - len(newend))
                        newend += newend[::-1]
                        mindiff, ans = comp(newend, mindiff, ans)
        else:
            mid = n // 2
            end = start[:mid] + start[mid] + start[:mid][::-1]
            mindiff, ans = comp(end, mindiff, ans)
            
            mv = int(start[mid])
            for v in [mv-1, mv+1]:
                if 0 <= v < 10:
                    end = start[:mid] + str(v) + start[:mid][::-1]
                    mindiff, ans = comp(end, mindiff, ans)
            
            mv = int(start[mid])
            if mv > 0:
                end = start[:mid] + str(mv-1) + start[mid+1:]
                mindiff, ans = comp(end, mindiff, ans)
            if mv < 0:
                end = start[:mid] + str(mv+1) + start[mid+1:]
                mindiff, ans = comp(end, mindiff, ans)

            for i in range(mid+1, n):
                j = 2 * mid - i
                # increase
                for k in range(j, -1, -1):
                    if int(start[k]) < 9:
                        newend = start[:k] + str(int(start[k]) + 1)
                        newend += '0' * (n // 2 - len(newend))
                        newend += '0' + newend[::-1]
                        mindiff, ans = comp(newend, mindiff, ans)
                        break
                # decrease
                for k in range(j, mid):
                    if (k > 0 and int(start[k]) > 0) or (k == 0 and int(start[k]) > 1):
                        newend = start[:k] + str(int(start[k]) - 1)
                        newend += '9' * (n // 2 - len(newend))
                        newend += '9' + newend[::-1]
                        mindiff, ans = comp(newend, mindiff, ans)
            
        return ans
        
        
s = Solution()
print(s.nearestPalindromic('11011'))
# print(s.nearestPalindromic('99'))
# print(s.nearestPalindromic('11'))
# print(s.nearestPalindromic('2222'))
# print(s.nearestPalindromic('1111'))
# print(s.nearestPalindromic('11'))
# print(s.nearestPalindromic('111'))
# print(s.nearestPalindromic('1234'))
# print(s.nearestPalindromic('123'))
# print(s.nearestPalindromic('12'))
# print(s.nearestPalindromic('1'))
# print(s.nearestPalindromic('429'))
# print(s.nearestPalindromic('357'))
# print(s.nearestPalindromic('1232432432423423432'))