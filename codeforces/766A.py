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
created by shhuan at 2017/11/24 22:20

"""

a = input()
b = input()

if a == b:
    print(-1)
elif len(a) > len(b):
    print(len(a))
else:
    print(len(b))



