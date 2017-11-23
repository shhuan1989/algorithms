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
created by shhuan at 2017/11/23 10:21

"""


n, d = map(int, input().split())

t = [int(x) for x in input().split()]

churu = d - sum(t)
if n==1:
    if churu >= 0:
        print(churu // 5)
        exit(0)
    else:
        print(-1)
        exit(0)



if churu <= 0:
    print(-1)
    exit(0)

# if churu % 5 != 0:
#     print(-1)
#     exit(0)

if churu // 5 < 2*(n-1):
    print(-1)
    exit(0)

print(churu// 5)
