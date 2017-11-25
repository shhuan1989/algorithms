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
created by shhuan at 2017/11/24 22:57

"""


# s->t, cost
# 1->n, 0
# n->2, 1
# 2->n-1, 0
# n-1,3, 1
#...
# n//2 -> n//+1, 0 ; n is even
#

# 2: 0
# 3: 1
# 4: 1
# 5: 2
# 6: 2
# 7: 3

N = int(input())
print((N-1)//2)