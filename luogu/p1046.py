# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/9

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    H = [int(x) for x in input().split()]
    K = int(input()) + 30
    
    print(len([v for v in H if v <= K]))