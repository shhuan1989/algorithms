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
created by shhuan at 2017/11/21 22:34

"""

s = input()

if s[0].islower() and all([v.isupper() for v in s[1:]]):
    print(s[0].upper() + "".join([v.lower() for v in s[1:]]))
elif all([v.isupper() for v in s]):
    print("".join([v.lower() for v in s]))
else:
    print(s)