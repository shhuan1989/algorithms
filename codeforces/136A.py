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
created by shhuan at 2017/11/21 23:40

"""

N = int(input())
P = [int(x) for x in input().split()]

mp = {v: i+1 for i, v in enumerate(P)}

ans = [mp[k] for k in sorted(mp.keys())]

print(" ".join(map(str, ans)))