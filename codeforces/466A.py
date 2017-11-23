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
created by shhuan at 2017/11/22 11:10

"""

N, M, A, B = map(int, input().split())

ans = N*A

if N % M == 0:
    ans = min(ans, N//M * B)
else:
    ans = min(ans, N//M*B+B, N//M*B + (N%M) *A)

print(ans)