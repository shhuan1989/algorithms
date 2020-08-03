# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/3

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    N = int(input())
    A = []
    vi = {}
    for i in range(N):
        A.append(input().strip())
        vi[A[-1]] = i
    
    send = [0 for _ in range(N)]
    receive = [0 for _ in range(N)]
    for i in range(N):
        name = input().strip()
        a, b = map(int, input().strip().split())
        if b > 0:
            c = a // b
            send[vi[name]] = a - a % b
            for i in range(b):
                to = input().strip()
                receive[vi[to]] += c
    for i, name in enumerate(A):
        print('{} {}'.format(name, receive[i]-send[i]))
