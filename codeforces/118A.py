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
created by shhuan at 2017/11/21 20:24

"""

S = input()

vowels = {"A", "O", "Y", "E", "U", "I"}
S = [x.upper() for x in S]
S = [x for x in S if x not in vowels]

S = [x.lower() for x in S]

if S:
    print("." + ".".join(S))
else:
    print("")
