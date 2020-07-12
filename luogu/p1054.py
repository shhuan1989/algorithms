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
created by shhuan at 2020/7/9 21:58

"""

def cal(s, t):
    if not t:
        return
    op = t.pop()
    b = s.pop()
    a = s.pop()
    if op == '+':
        s.append(a + b)
    elif op == '-':
        s.append(a - b)
    elif op == '*':
        s.append(a * b)
    elif op == '/':
        s.append(a // b)
    else:
        s.append(a ** b)

def solve(exp, val):
    exp = exp.replace(' ', '')
    s = []
    t = []
    i = 0
    n = len(exp)
    while i < n:
        v = exp[i]
        if v.isdigit():
            k = i + 1
            w = int(v)
            for j in range(i+1, n):
                u = exp[j]
                k = j
                if not u.isdigit():
                    break
                w *= 10
                w += int(u)
            if k < n and exp[k].isdigit():
                k += 1
            i = k
            s.append(w)
        elif v == '(':
            t.append(v)
            i += 1
        elif v == '^':
            t.append(v)
            i += 1
        elif v == '*' or v == '-':
            while t and t[-1] == '^':
                cal(s, t)
            t.append(v)
            i += 1
        elif v == 'a':
            s.append(val)
            i += 1
        elif v == ')':
            while t:
                if t[-1] == '(':
                    t.pop()
                    break
                cal(s, t)
            i += 1
        else:
            while t and t[-1] in {'*', '/', '^'}:
                cal(s, t)
            t.append(v)
            i += 1

    while t:
        cal(s, t)

    return s[0]


if __name__ == '__main__':
    exp = input()
    N = int(input())
    ans = []
    for i in range(N):
        a = input()
        if all([solve(exp, i) == solve(a, i) for i in range(10)]):
            ans.append(i)

    print(''.join([chr(ord('A') + v) for v in ans]))