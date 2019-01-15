# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/19/18

"""

import collections
import time
import os
import sys
import bisect
import heapq
import random

x1, y1, x2, y2 = 0, 0, 10**9, 10**9

N = int(input())
# N = 30
for i in range(N):
    x, y = x1 + (x2-x1)//4, y1 + 3*(y2-y1)//4
    
    print('{} {}'.format(x, y))
    sys.stdout.flush()
    
    color = input()
    # color = 'black' if random.randint(1, 10) < 5 else 'white'
    # color = 'black'
    if color == 'black':
        x1, y1 = x, y
    else:
        x2, y2 = x, y


print('{} {} {} {}'.format(x1+1, y1, x2-1, y2))
    

