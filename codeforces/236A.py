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
created by shhuan at 2017/11/21 22:53

"""

s = input()

s = set(s)

if len(s) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")