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
created by shhuan at 2017/11/24 23:42

"""


s = [int(x) for x in list(input())]

for i, v in enumerate(s):
    if v != 1 and v != 4:
        print("NO")
        exit(0)
    if v == 4:
        if i == 0:
            print("NO")
            exit(0)
        elif s[i-1] == 4:
            if i < 2:
                print("NO")
                exit(0)
            if s[i-2] != 1:
                print("NO")
                exit(0)

print("YES")