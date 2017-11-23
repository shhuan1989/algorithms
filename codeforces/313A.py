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
created by shhuan at 2017/11/22 11:14

"""


n = int(input())


if n > 0:
    print(n)
else:
    n = abs(n)
    if n < 10:
        print(0)
    elif n < 100:
        print(max(-n, 0-n//10, 0-(n%10)))
    else:
        sn = str(n)
        last = str(n % 10)
        last2 = str(n // 10 % 10)
        print(max(-n, -int(sn[:-2]+last), -int(sn[:-2]+last2)))
