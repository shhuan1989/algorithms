# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        
        def dfs(exp):
            if not exp:
                return True
            
            # find and or
            c = 0
            for i, v in enumerate(exp):
                if v == '(':
                    c += 1
                elif v == ')':
                    c -= 1
                if c == 0 and 0 < i < len(exp)-1:
                    a = dfs(exp[:i])
                    b = dfs(exp[i+1:])
                    if i+1 < len(exp):
                        if exp[i+1] == '|':
                            return a or b
                        elif exp[i+1] == '&':
                            return a and b
                    return a and b
                
            if exp[0] == '(':
                return dfs(exp[1: len(exp)-1])
            elif exp[0] == '!':
                r = True
                i = 1
                while i < len(exp) and exp[i] == '!':
                    r = not r
                    i += 1
                if exp[i] == 't':
                    return True if not r else False
                elif exp[i] == 'f':
                    return False if not r else True
                elif exp[i] == '(':
                    c = 1
                    i += 1
                    l = i
                    while i < len(exp):
                        if exp[i] == '(':
                            c += 1
                        elif exp[i] == ')':
                            c -= 1
                        if c == 0:
                            a = dfs(exp[l: i])
                            return a if not r else not a
                        i += 1
            elif exp[0] == '|':
                l = 2
                i = 2
                c = 0
                while i < len(exp):
                    if exp[i] == '(':
                        c += 1
                    elif exp[i] == ')':
                        c -= 1
                    if c == 0 and exp[i+1] in {',' , ')'}:
                        if dfs(exp[l: i+1]):
                            return True
                        l = i + 2
                        i += 1
                        
                    i += 1
                return False
            elif exp[0] == '&':
                l = 2
                i = 2
                c = 0
                while i < len(exp):
                    if exp[i] == '(':
                        c += 1
                    elif exp[i] == ')':
                        c -= 1
                    if c == 0 and exp[i + 1] in {',', ')'}:
                        if not dfs(exp[l: i+1]):
                            return False
                        l = i + 2
                        i += 1
        
                    i += 1
                return True
            else:
                if len(exp) == 1:
                    return True if exp == 't' else False
        
        return dfs(expression)
    

s = Solution()
print(s.parseBoolExpr('|(&(t,f,t),!(t))') == False)
print(s.parseBoolExpr('!(f)') == True)
print(s.parseBoolExpr('|(f,t)') == True)
print(s.parseBoolExpr('&(t,f)') == False)
print(s.parseBoolExpr('|(&(t,f,t),!(t))') == False)
