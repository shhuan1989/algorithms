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
created by shhuan at 2017/11/22 22:47

"""

a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

n = int(input())

cup = a1 + a2 + a3
medal = b1 + b2 + b3

a = cup//5 if cup % 5 == 0 else cup//5+1
b = medal//10 if medal % 10 == 0 else medal//10+1

if a+b <= n:
    print("YES")
else:
    print("NO")

