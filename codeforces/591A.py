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
created by shhuan at 2017/11/24 22:53

"""

L = int(input())

p = int(input())
q = int(input())


# t*p + t*q == L
# t = L/(p+q)
# s = p*t


print(p*L/(p+q))