# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/30

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
    for i in range(N):
        x, y = map(int, input().split())
        A.append((x, y))
    A.sort()
    # print(A)
    mx, my = (A[0][0] + A[-1][0]) / 2, (A[0][1] + A[-1][1]) / 2
    for i in range((N+1)//2):
        cx, cy = (A[i][0] + A[N-i-1][0]) / 2, (A[i][1] + A[N-i-1][1]) / 2
        if abs(cx-mx) > 0.01 or abs(cy-my) > 0.01:
            print("This is a dangerous situation!")
            exit(0)

    print("V.I.P. should stay at ({:.1f},{:.1f}).".format(mx, my))

        