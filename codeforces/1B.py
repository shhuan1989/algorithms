# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
import re
"""
created by shhuan at 2017/11/24 14:29

"""


N = int(input())


def num2alpha(val):
    a = [chr(ord("A")+i) for i in range(26)]

    ans = ""
    while val > 0:
        ans += a[val % 26 - 1]

        if val % 26 == 0:
            val -= 1
            val //= 26
        else:
            val //= 26


    return ans[::-1]


def alpha2num(val):

    ans = 0
    for v in val:
        ans *= 26
        ans += ord(v)-ord("A")+1

    return ans

for i in range(N):
    s = input()

    if re.match("R\d\d*C\d\d*", s):
        # R23C55
        m = s.find("C")
        c = int(s[m+1:])
        print(num2alpha(c)+s[1:m])
    else:
        m = -1
        for i in range(len(s)):
            if s[i].isnumeric():
                m = i
                break

        print("R"+s[m:]+"C"+str(alpha2num(s[:m])))