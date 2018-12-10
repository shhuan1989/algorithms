# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/10/18

"""
import math

N = int(input())
a, b = map(int, input().split())
# wcd = {a, b}
#
#
# def gcd(x, y):
#     while y:
#         x, y = y, x%y
#
#     return x
#
#
# for i in range(N-1):
#     a, b = map(int, input().split())
#     wcd = {gcd(x, a) for x in wcd} | {gcd(x, b) for x in wcd}
#     wcd.discard(1)
#
#     if not wcd:
#         print(-1)
#         exit(0)
#
# print(min(wcd))


def factorize(val):
    fs = set()
    i = 2
    while i <= int(math.sqrt(val)) + 1:
        if val % i == 0:
            fs.add(i)
            while val % i == 0:
                val //= i
        i += 1
    if val > 1:
        fs.add(val)
    return fs
    

factors = factorize(a) | factorize(b)
for i in range(N-1):
    a, b = map(int, input().split())
    factors = {v for v in factors if a % v == 0 or b % v == 0}
    if not factors:
        print(-1)
        exit(0)
print(min(factors))



