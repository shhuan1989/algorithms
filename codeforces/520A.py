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
created by shhuan at 2017/11/22 01:43

"""

N = int(input())
S = input()

S = {v.lower() for v in S}

if len(S) == 26:
    print("YES")
else:
    print("NO")
