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



# a-x == a^x
# a 的某一位等于0，x的这个位也只能等于0，否则x的这一位01都行

N = int(input())

for i in range(N):
    V = int(input())
    V = bin(V)[2:]
    
    res = 2 ** (sum([int(x) for x in V]))
    
    print(res)