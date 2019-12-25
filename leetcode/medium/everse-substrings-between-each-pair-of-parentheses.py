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


class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        def dfs(u):
            if not u:
                return ''

            i = u.find('(')
            if i < 0:
                return u
            
            if i == 0:
                k, l, r = 0, 0, 0
                while r < len(u):
                    v = u[r]
                    if v == '(':
                        k += 1
                    elif v == ')':
                        k -= 1
                    if k == 0:
                        return dfs(u[1: r])[::-1] + dfs(u[r+1:])
                    r += 1
            else:
                return u[:i] + dfs(u[i:])
        
        return dfs(s)
                
    
s = Solution()
print(s.reverseParentheses('(abcd)'))
print(s.reverseParentheses('(u(love)i)'))
print(s.reverseParentheses('(ed(et(oc))el)'))
print(s.reverseParentheses('a(bcdefghijkl(mno)p)q'))