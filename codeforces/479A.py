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
created by shhuan at 2017/11/21 23:46

"""

a = int(input())
b = int(input())
c = int(input())

ans = max(a*b*c, a+b*c, a*b+c, a+b+c, (a+b)*c, a*(b+c))

print(ans)