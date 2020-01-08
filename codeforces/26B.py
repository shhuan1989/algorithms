# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/2/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


s = input()

c = 0
ans = 0
for i, v in enumerate(s):
    if v == '(':
        c += 1
    else:
        c -= 1
        if c >= 0:
            ans += 1
        else:
            c = 0

print(ans * 2)