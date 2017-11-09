# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/8 23:19

"""


T = int(input())


def make_pal(cs, l, n):
    s = "".join([cs[random.randint(0, len(cs)-1)] for _ in range(n)])


    for i in range(n):

        k = 1
        if l % 2 == 0:
            while k < l//2 and s[i-k] == s[i+k]:
                k += 1
            if k == l//2:
                for c in cs:
                    if c != s[i-1]:
                        s[i+k] = c
                        break
                if s[i+k] == s[i-k]:
                    return ''
        else:
            # while k <= l//2 and s[]
            pass
        



for ti in range(T):
    N, A = map(int, input().split())

    L = 2
    cs = [chr(i+ord('a')) for i in range(A)]

    lo = 1
    hi = N
    s = ''
    while lo < hi:
        L = (lo+hi)//2
        s = make_pal(cs, L)
        if s:
            hi = L
        else:
            lo = L + 1

    print(L, s)