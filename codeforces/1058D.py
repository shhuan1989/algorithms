# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/8/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys



N, M, K = map(int, input().split())

if 2*N*M % K == 0:
    print('YES')
else:
    print('NO')