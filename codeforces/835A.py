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
created by shhuan at 2017/11/24 22:38

"""


s, v1, v2, t1, t2 = map(int, input().split())

ta = s*v1 + 2*t1
tb = s*v2 + 2*t2

if ta == tb:
    print("Friendship")
elif ta < tb:
    print("First")
else:
    print("Second")