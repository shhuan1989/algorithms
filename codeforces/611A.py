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
created by shhuan at 2017/11/24 19:44

"""

s = input()
a = s.split()

v = int(a[0])

type = a[2]
if type == "week":
    if v == 5 or v == 6:
        print(53)
    else:
        print(52)
else:
    if v == 30:
        print(11)
    elif v == 31:
        print(7)
    else:
        print(12)