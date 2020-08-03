# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/17

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List



def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        
    return x > 1


if __name__ == '__main__':
    s = input()
    wc = collections.Counter(s.strip())
    diff = max(wc.values()) - min(wc.values())
    
    if isprime(diff):
        print("Lucky Word")
        print(diff)
    else:
        print("No Answer")
        print(0)