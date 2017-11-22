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
created by shhuan at 2017/11/22 01:06

"""

S = input()

upper = len([x for x in S if x.isupper()])

if upper > len(S)-upper:
    print("".join([x.upper() for x in S]))
else:
    print("".join([x.lower() for x in S]))