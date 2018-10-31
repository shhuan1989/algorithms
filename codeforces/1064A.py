# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/17/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys



A = [int(x) for x in input().split()]
A.sort()

print(max(0, A[2]-A[0]-A[1]+1))


