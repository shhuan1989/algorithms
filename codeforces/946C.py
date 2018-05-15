# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 3/8/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

s = [x for x in input()]


t = 'abcdefghijklmnopqrstuvwxyz'


si = 0
for u in t:
    if si >= len(s):
        print(-1)
        exit(0)

    while si < len(s) and s[si] > u:
        si += 1
    if si < len(s):
        s[si] = u
        si += 1
    else:
        print(-1)
        exit(0)

print(''.join(s))
