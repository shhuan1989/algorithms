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
created by shhuan at 2017/11/22 00:13

"""

N = int(input())

if N % 5 == 0:
    print(N // 5)
else:
    print(N//5+1)