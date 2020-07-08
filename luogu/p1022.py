# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

def isop(v):
    return v == '+' or v == '-'


def parse(exp):
    q = []
    for i, v in enumerate(exp):
        if isop(v):
            if not q:
                q.append(0)
            q.append(v)
        elif v.isdigit():
            if q and isinstance(q[-1], int):
                q.append(q.pop() * 10 + int(v))
            else:
                q.append(int(v))
        else:
            q.append(v)
    return q



def getparam(exp, x):
    vx, vv = 0, 0
    for i in range(len(exp)):
        v = exp[i]
        if v == x:
            if isinstance(exp[i-1], int):
                if i - 2 >= 0:
                    if exp[i-2] == '+':
                        vx += exp[i-1]
                    elif exp[i-2 ] == '-':
                        vx -= exp[i-1]
                else:
                    vx += exp[i-1]
            else:
                if i - 1 >= 0:
                    if exp[i-1] == '+':
                        vx += 1
                    else:
                        vx -= 1
                else:
                    vx += 1
    
    for i in range(len(exp)):
        v = exp[i]
        if isinstance(v, int):
            if i+1 >= len(exp) or exp[i+1] != x:
                if i-1 >= 0:
                    if exp[i-1] == '-':
                        vv -= v
                    else:
                        vv += v
                else:
                    vv += v
    
    return vx, vv

def solve(exp):
    a, b = exp.split('=')
    pa, pb = parse(a), parse(b)
    x = [v for v in exp if v.isalpha() and v != '+' and v != '-'][0]
    
    xa, va = getparam(pa, x)
    xb, vb = getparam(pb, x)
    
    # print(pa, xa, va)
    # print(pb, xb, vb)
    
    xx = xa-xb
    vv = vb-va
    ans = vv/xx
    if abs(ans) < 1e-6:
        ans = 0.0
    
    return x, ans
    


if __name__ == '__main__':
    exp = input()
    x, v = solve(exp)
    print('{}={:.3f}'.format(x, v))
