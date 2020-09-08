# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/8

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

MOD = 10007


if __name__ == '__main__':
    # sys.stdin = open('P1310_2.in', 'r')
    N = int(input())
    exp = input().strip()

    a, b = [], []
    
    def work():
        op = a.pop()
        one1, zero1 = b.pop()
        one2, zero2 = b.pop()
        if op == '*':
            one = one1 * one2
            one %= MOD
            zero = (zero1 * zero2 + zero1 * one2 + zero2 * one1)
            zero %= MOD
            return (one, zero)
        else:
            zero = zero1 * zero2
            zero %= MOD
            one = (zero1 * one2 + zero2 * one1 + one1 * one2)
            one %= MOD
            return (one, zero)
    
    for i, v in enumerate(exp):
        if v == '(':
            a.append(v)
        elif v == ')':
            while a[-1] != '(':
                b.append(work())
            a.pop()
        else:
            op = v
            if op == '+':
                while a and a[-1] == '*':
                    b.append(work())
                    
            a.append(op)
            if i == 0 or exp[i-1] == '(':
                b.append((1, 1))
            if i + 1 >= len(exp) or exp[i+1] != '(':
                b.append((1, 1))
    
    while a:
        b.append(work())
        
    print(b[0][1])