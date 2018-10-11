# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 9/28/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


N, D = map(int, input().split())
M = int(input())


def inField(x, y):
    
    return D <= x+y <= 2*N-D and x-D <= y <= D+x



for i in range(M):
    x, y = map(int, input().split())
    if inField(x, y):
        print('YES')
    else:
        print('NO')