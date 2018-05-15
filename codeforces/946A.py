# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 3/8/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

N = int(input())

A = map(int, input().split())

ans = sum([abs(x) for x in A])

print(ans)