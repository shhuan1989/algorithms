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
created by shhuan at 2017/11/21 20:36

"""

a = input()
b = input()

a = "".join([x.lower() for x in a])
b = "".join([x.lower() for x in b])

if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)