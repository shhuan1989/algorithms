# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 10/19/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
def countOne(num):
    # 计算数字的二进制表示的1的个数
    return len([x for x in bin(num)[2:] if x == '1'])

def solve(nums):
    N = len(nums)
    ones = [countOne(x) for x in nums]

    res = 0
    sufSum = 0
    s0, s1 = 1, 0

    for i in range(N-1, -1, -1):
        sm, mx = 0, 0
        add = 0
        for j in range(i, min(N, i+65)):
            sm += ones[j]
            mx = max(mx, ones[j])
            if mx > sm - mx and sm % 2 == 0:
                add -= 1

        sufSum += ones[i]
        add += s0 if sufSum & 1 == 0 else s1
        res += add

        if sufSum & 1:
            s1 += 1
        else:
            s0 += 1

    return res


N = int(input())
nums = [int(x) for x in input().split()]
#
# nums = [1000000000000000000, 352839520853234088, 175235832528365792, 753467583475385837, 895062156280564685]
# nums = [6, 7, 14]
# nums = [1, 2, 1, 16]
print(solve(nums))

