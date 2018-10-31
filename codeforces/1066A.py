# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/19/18



"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


T = map(int, input())
for ti in range(T):
    L, v, l, r = map(int, input().split())
    
    total = L // v
    