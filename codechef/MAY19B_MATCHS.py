# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-05-05

"""

import collections
import time
import os
import sys
import bisect
import heapq

memo = {}


def solve(n, m):
    if n < m:
        return solve(m, n)
    
    if m == 0 or n == 0:
        return 0
    
    if n % m == 0:
        return 1
    
    key = (n, m)
    if key in memo:
        return memo[key]
    
    mex = set()
    k = m
    while k <= n:
        mex.add(solve(n - k, m))
        k += m
    
    res = 0
    while True:
        if res not in mex:
            memo[key] = res
            return res
        res += 1
        
def f1(n, m):
    if n < m:
        n, m = m, n
        
    games = []
    while n and m:
        if n % m == 0:
            games.append(1)
            break
        else:
            games.append(n // m)
        n, m = m, n % m
    # print(games)
    
    win = False
    for v in reversed(games):
        if not win:
            win = True
        else:
            win = v > 1
    
    return win
#
# for a in range(2, 100):
#     for b in range(a+1, 100):
#         x = solve(a, b) > 0
#         if x != f1(a, b):
#             print(a, b)
#
#
# print(solve(5, 7) > 0)
# print(f1(5, 7))

    
# f1(123123, 32)
# f1(1, 1)


#
#
# memo = {}
#
# def solve(n, m):
#     if n < m:
#         return solve(m, n)
#
#     if m == 0 or n == 0:
#         return 0
#
#     if n % m == 0:
#         return 1
#
#     key = (n, m)
#     if key in memo:
#         return memo[key]
#
#
#     k = m // n
#
#     mex = {solve(n % m , m)}
#
#     res = 0
#     while True:
#         if res not in mex:
#             memo[key] = res
#             return res
#         res += 1
#
#
# import random
# for i in range(100):
#     a = random.randint(10**15, 10**17)
#     b = random.randint(10 ** 15, 10 ** 17)
#     print(solve(a, b))
#
#
T = int(input())
for ti in range(T):
    n, m = map(int, input().split())
    a = f1(n, m)
    if a:
        print('Ari')
    else:
        print('Rich')

    