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
created by shhuan at 2017/11/22 23:02

"""


A = []

weights = {
    "Q": 9,
    "R": 5,
    "B": 3,
    "N": 3,
    "P": 1,
    "K": 0,
    ".": 0
}

a = 0
b = 0
for i in range(8):
    row = input()
    for v in row:
        if v.islower():
            b += weights[v.upper()]
        else:
            a += weights[v]

if a > b:
    print("White")
elif a < b:
    print("Black")
else:
    print("Draw")