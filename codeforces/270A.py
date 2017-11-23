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
created by shhuan at 2017/11/22 22:04

已知正多边形内角度数则其边数为：360°÷（180°－内角度数）

"""

N = int(input())

for i  in range(N):
    a = int(input())

    if 360 % (180 - a) == 0:
        print("YES")
    else:
        print("NO")