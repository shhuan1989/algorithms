# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


sys.setrecursionlimit(200000)
if __name__ == '__main__':
    # sys.stdin = open('p1322.in', 'r')
    exp = input().strip()
    
    exp = exp.replace('REPEAT', '*')
    exp = exp.replace('BK', '-')
    exp = exp.replace('FD', '+')
    tokens = []
    i = 0
    n = len(exp)
    while i < n:
        if exp[i] in {'*', '+', '-', '[', ']'}:
            tokens.append(exp[i])
            i += 1
        elif exp[i].isdigit():
            j = i + 1
            while j < n and exp[j].isdigit():
                j += 1
            tokens.append(int(exp[i: j]))
            i = j
        else:
            i += 1
    
    # print(tokens)
    
    ops = []
    ps = []
    i = 0
    n = len(tokens)
    
    def dowork():
        op = ops.pop()
        a = ps.pop()
        b = ps.pop()
        if op == '+':
            ps.append(a + b)
        elif op == '-':
            ps.append(b - a)
        elif op == '*':
            ps.append(a * b)
        
    while i < n:
        v = tokens[i]
        if v == '[':
            ops.append(v)
            i += 1
        elif v == ']':
            while ops and ops[-1] != '[':
                dowork()
            ops.pop()
            i += 1
        elif v == '*':
            if not ops or ops[-1] == '[':
                ps.append(0)
            ops.append('+')
            ops.append(v)
            ps.append(tokens[i+1])
            i += 2
        elif v in ['+', '-']:
            while ops and ops[-1] == '*':
                dowork()
            if not ops or ops[-1] == '[':
                ps.append(0)
            ops.append(v)
            ps.append(tokens[i+1])
            i += 2
        else:
            i += 1
    
    while ops:
        dowork()
    
    print(abs(ps[0]))
    
    