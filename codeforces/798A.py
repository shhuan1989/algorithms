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
created by shhuan at 2017/11/24 23:18

"""

s = list(input())

def check(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False

    return True


for i in range(len(s)):
    v = s[i]
    for c in [chr(ord('a')+i) for i in range(26)]:
        if c == v:
            continue
        s[i] = c
        if check(s):
            print("YES")
            exit(0)
    s[i] = v

print("NO")