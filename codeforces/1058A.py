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

N = int(input())
A = [int(x) for x in input().split()]

if all(x == 0 for x in A):
    print('EASY')
else:
    print('HARD')