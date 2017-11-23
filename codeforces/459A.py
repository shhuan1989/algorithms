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
created by shhuan at 2017/11/23 11:11

"""

x1, y1, x2, y2 = map(int, input().split())


if x1 == x2 and y1 == y2:
    print(-1)
else:
    if x1 == x2:
        d = abs(y1-y2)
        print(x1+d, y1, x2+d, y2)
    elif y1 == y2:
        d = abs(x1-x2)
        print(x1, y1+d, x2, y2+d)
    else:
        if abs(x1-x2) != abs(y1-y2):
            print(-1)
        else:
            d = abs(x1-x2)
            print(x1, y2, x2, y1)
