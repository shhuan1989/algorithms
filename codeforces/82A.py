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
created by shhuan at 2017/11/22 00:47

"""


# 1   6 7       16 17 18 19
# 2   8 9       20 21 22 23
# 3   10 11     24 25 26 27
# 4   12 13     28 29 30 31
# 5   14 15     32 33 34 35

# 2^0 + 2^1 + .. + 2^n = 2^(n+1)-1
# 5*(2^(n+1)-1) < N

N = int(input())

n = int(math.log(N//5+1, 2)) - 1

pre = 5*(2**(n+1)-1)

crew = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard" ]
print(crew[(N-pre-1) // (2**(n+1))])






