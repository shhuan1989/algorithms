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
import math

def mypow(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    a = mypow(n // 2)
    b = 1 if n % 2 == 0 else 2
    
    # print(n, a*a*b)
    c = a * a * b
    if len(str(c)) > 500:
        c = int(str(c)[-500:])
    
    return c
    
    


if __name__ == '__main__':
    P = int(input())
    
    bits = int(math.log(2**P, 10)) + 1
    print(bits)
    ans = str(mypow(P)-1)
    ans = ans[-500:]
    ans = '0'*(500-len(ans)) + ans
    for i in range(0, 500, 50):
        print(ans[i: i+50])
