import math
import os
import random
import re
import sys
from typing import List
import bisect
import collections
import heapq

import numpy as np


def cal(path):
    with open(path, 'r') as f:
        a, b = [], []
        for line in f.readlines():
            line = line.strip()
            m = re.search('^(\d+(\.\d+))\s*%$', line)
            if m:
                a.append(float(m.group(1)))
            
            if re.fullmatch('^\d+$', line):
                b.append(float(line))
        
        a1 = np.average(a[::2])
        a2 = np.average(a[1::2])
        print(a1, a2)
        
        # print(a, b)
        # aa = np.average(a) * 1000
        # ab = np.average(b)
        # print(aa, ab, ab / (aa + ab))
        



cal('/Users/shuangquan.huang/Desktop/a.txt')
# cal('/Users/shuangquan.huang/Desktop/b.txt')