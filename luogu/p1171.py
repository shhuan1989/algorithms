# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/21

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
from functools import lru_cache
from memory_profiler import profile

INF = 10 ** 6 + 5


def solve(N, W):
    # for k in range(N):
    #     for i in range(N):
    #         for j in range(N):
    #             W[i][j] = min(W[i][j], W[i][k] + W[k][j])

    def bit_set(v, i):
        return (v & (1 << i)) > 0

    def set_bit(v, i):
        return v | (1 << i)

    def unset_bit(v, i):
        return set_bit(v, i) ^ (1 << i)

    def getstate(s, index, count):
        if count <= 0:
            return [s]

        if index >= N:
            return []

        if bit_set(s, index):
            return getstate(s, index + 1, count)

        return getstate(s, index + 1, count) + getstate(set_bit(s, index), index + 1, count - 1)

    dp = [[INF for _ in range(2 ** N)] for _ in range(N)]
    dp[0][1] = 0

    init = 1
    for k in range(2, N + 1):
        for end in range(1, N):
            for s in getstate(set_bit(init, end), 0, k - 2):
                for pi in range(N):
                    if pi != end and bit_set(s, pi):
                        dp[end][s] = min(dp[end][s], dp[pi][unset_bit(s, end)] + W[pi][end])

    ans = INF
    for i in range(1, N):
        ans = min(ans, dp[i][2 ** N - 1] + W[i][0])
    print(ans)

    # @lru_cache(maxsize=None)
    # def dfs(curr, state):
    #     if curr == 0 and state == 1:
    #         return 0
    #
    #     ans = INF
    #     for pre in range(1, N):
    #         if pre != curr and bit_set(state, pre):
    #             ans = min(ans, W[pre][curr] + dfs(pre, unset_bit(state, curr)))
    #
    #     if bit_set(state, 0) and len([1 for i in range(1, N) if bit_set(state, i)]) == 1:
    #         ans = min(ans, W[0][curr] + dfs(0, 1))
    #
    #     return ans
    #
    # ans = INF
    # for i in range(1, N):
    #     ans = min(ans, dfs(i, 2**N-1) + W[i][0])
    # print(ans)


@profile
def main():
    N = int(input())
    INF = 10 ** 6
    W = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        row = [int(x) for x in input().strip().split()]
        for j in range(N):
            W[i][j] = row[j]
    solve(N, W)

if __name__ == '__main__':
    sys.stdin = open('p1171_2.in', 'r')
    main()

    # import random
    # for i in range(1):
    #     N = 20
    #     W = [[random.randint(1, 1000) for _ in range(N)] for _ in range(N)]
    #     for i in range(N):
    #         W[i][i] = 0
    #
    #     t0 = time.time()
    #     solve(N, W)
    #     print(time.time() - t0)

