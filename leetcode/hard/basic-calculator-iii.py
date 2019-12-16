# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/16 21:41

"""

class Solution:
    def calculate(self, s: str) -> int:

        def check(exp):
            c, i = 0, 0
            for i, v in enumerate(exp):
                if v == '(':
                    c += 1
                elif v == ')':
                    c -= 1

            return c == 0

        def dfs(exp):
            if not exp:
                return 0

            if all([v.isdigit() for v in exp]):
                return int(exp)

            hasaddop, addresult, left, add = False, 0, 0, True
            for i, v in enumerate(exp):
                if v in {'+', '-'}:
                    if check(exp[left: i]):
                        hasaddop = True
                        part = dfs(exp[left: i])
                        if add:
                            addresult += part
                        else:
                            addresult -= part
                        left = i + 1
                        add = v == '+'
            if 0 < left:
                part = dfs(exp[left:])
                if add:
                    addresult += part
                else:
                    addresult -= part
            if hasaddop:
                return addresult

            hasmul, mulresult, left, mul = False, 1, 0, True

            for i, v in enumerate(exp):
                if v in {'*', '/'}:
                    if check(exp[:i]):
                        hasmul = True
                        part = dfs(exp[left: i])
                        if mul:
                            mulresult *= part
                        else:
                            mulresult //= part
                        mul = v == '*'
                        left = i+1
            if 0 < left:
                part = dfs(exp[left:])
                if mul:
                    mulresult *= part
                else:
                    mulresult //= part
            if hasmul:
                return mulresult

            if exp[0] == '(' and exp[-1] == ')':
                return dfs(exp[1: -1])

            return 0

        return dfs(s.replace(' ', ''))

s = Solution()
print(s.calculate('10/2/5'))
print(s.calculate('1 + 1'))
print(s.calculate(' 6-4 / 2 '))
print(s.calculate('2*(5+5*2)/3+(6/2+8)'))
print(s.calculate('(2+6* 3+5- (3*14/7+2)*5)+3'))
print(s.calculate('1*2-3/4+5*6-7*8+9/10'))