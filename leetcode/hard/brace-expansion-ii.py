# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/13/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        
        def dfs(exp):
            c = 0
            l, i, firstmath = 0, 0, 0
            parts = []
            while i < len(exp):
                if exp[i] == '{':
                    c += 1
                elif exp[i] == '}':
                    c -= 1
                
                if c == 0:
                    if firstmath <= 0:
                        firstmath = i
                    if i + 1 < len(exp) and exp[i+1] == ',':
                        parts.append(exp[l: i+1])
                        i += 1
                        l = i + 1
                i += 1
            if i > l:
                parts.append(exp[l: i])
            if len(parts) == 1:
                if exp[0] == '{' and firstmath == len(exp) - 1:
                    return dfs(exp[1: -1])
                else:
                    parts = []
                    c = 0
                    i = exp.find('{')
                    if i > 0:
                        parts.append(exp[:i])
                    elif i < 0:
                        parts = [exp]
                        i = len(exp)
                        
                    l = i + 1
                    while i < len(exp):
                        if exp[i] == '{':
                            c += 1
                        elif exp[i] == '}':
                            c -= 1
                        if c == 0:
                            parts.append(exp[l: i])
                            l = i + 1
                            i = exp.find('{', i)
                            if i > l:
                                parts.append(exp[l: i])
                                c = 1
                                l = i + 1
                            elif i >= 0:
                                l = i + 1
                                c = 1
                            else:
                                if l < len(exp):
                                    parts.append(exp[l:])
                                break
                        i += 1
                    if i > l:
                        parts.append(exp[l: i])
                    
                    if len(parts) == 1:
                        return {exp}
                    
                    x = [dfs(p) for p in parts]
                    ans = x[0]
                    for i in range(1, len(x)):
                        ans = {a+y for a in ans for y in x[i]}
                    return ans
            
            ans = set()
            for p in parts:
                ans |= dfs(p)
            
            return ans

        
        expression = expression.replace(' ', '')
        return list(sorted(dfs(expression)))
    
        
s = Solution()
print(s.braceExpansionII('{a, b}'))
print(s.braceExpansionII('a'))
print(s.braceExpansionII('a{b,c}'))
print(s.braceExpansionII('{a,b}{c{d,e}}'))
print(s.braceExpansionII('{ab, z}'))
print(s.braceExpansionII('a{b, c}'))
print(s.braceExpansionII('{a{b, c}, {ab, z}}'))
print(s.braceExpansionII('{{a,z}, a{b,c}, {ab,z}}'))