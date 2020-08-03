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


def solve(N, K):
    K -= 1
    if K == 0:
        return 0
    ans = []
    for i in range(1, N + 1):
        if K == 0:
            break
        if K <= 1 << (N - i):
            ans.append(i)
            K -= 1
        else:
            K -= 1 << (N - i)
    return ' '.join(map(str, ans))


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    print(solve(N, K))