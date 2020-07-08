# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/6/9


从N个数字中任意去K个数，然后组合成一个新数。
规则是对于二进制的中每一位，如果至少有max(k-2, 1)个数字这一位是1，那么结果的这一位也是1。

1， 如果K<=3，那么结果就是这三个数字的取或
2， 鸽子洞原理，如果K>3，如果第i位设置成1，那么至少有K-2个数字这一位是1，即最多两个数字这一位不是1。
    根据鸽子洞原理，任取三个数字，至少有一个这一位是1. 即如果K位能够取到的最大值，其中存在三个数字取得的结果等于它。
    
    
"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, A):
    if N == 1:
        return A[0]
    elif N == 2:
        return A[0] | A[1]

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                ans = max(ans, A[i] | A[j] | A[k])

    return ans


N = int(input())
A = [int(x) for x in input().split()]
print(solve(N, A))