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
created by shhuan at 2017/11/22 10:20

"""

N, H = map(int, input().split())

A = [int(x) for x in input().split()]


a = len([x for x in A if x <= H])
b = N-a

print(a+b*2)