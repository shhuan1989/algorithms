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
created by shhuan at 2017/11/23 20:08

"""

s = input()




def check(s, m):

    vowels = ["A", "E", "I", "O", "U", "Y"]
    n = len(s)

    # dp[i]=1 means can reach previous i places, that is s[i-1]
    dp = [0] * (n + 2)
    dp[0] = 1

    for i in range(n + 2):
        if dp[i]:
            if i + m > n:
                return True

            for j in range(m):
                k = i + j
                if k >= n:
                    break
                if s[k] in vowels:
                    dp[k+1] = 1

    return dp[n+1]

i = 1
while not check(s, i):
    i += 1

print(i)