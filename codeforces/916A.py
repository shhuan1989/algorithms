# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/24/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

MOD = 24 * 60
X = int(input()) % MOD
H, M = map(int, input().split())

ans = 0
while ''.join(map(str, [H, M])).find('7') < 0:
    t = (H*60 + M - X + MOD) % MOD
    H = t // 60
    M = t % 60
    ans += 1

print(ans)