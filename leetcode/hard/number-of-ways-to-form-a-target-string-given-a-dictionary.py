# -*- coding: utf-8 -*-

"""
created by shhuan at 2021/1/24 16:23

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        if not words:
            return 0

        mod = 10 ** 9 + 7

        n = len(target)
        m = len(words[0])
        dp = [[0 for _ in range(m)] for _ in range(2)]
        presum = [[0 for _ in range(m)] for _ in range(2)]

        for i, w in enumerate(words):
            for k in range(m):
                if w[k] == target[0]:
                    dp[0][k] += 1

        presum[0][0] = dp[0][0]
        for i in range(1, m):
            presum[0][i] = presum[0][i-1] + dp[0][i]


        chindexcount = {}
        for ch in [chr(ord('a') + i) for i in range(26)]:
            chindexcount[ch] = collections.defaultdict(int)
        for i, w in enumerate(words):
            for j, ch in enumerate(w):
                chindexcount[ch][j] += 1

        for i in range(1, n):
            for k in range(m):
                # pre = sum(dp[i - 1][pk] for pk in range(k))
                # curr = len([1 for w in words if w[k] == target[i]])
                curr = chindexcount[target[i]][k]
                dp[i % 2][k] = ((presum[(i+1) % 2][k-1] if k-1 >= 0 else 0) * curr) % mod
                presum[i % 2][k] = dp[i % 2][k] + (presum[i % 2][k-1] if k-1 >= 0 else 0)

        return sum(dp[(n-1) % 2]) % mod


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(words=["acca", "bbbb", "caca"], target="aba"))
    print(s.numWays(words=["abba", "baab"], target="bab"))
    print(s.numWays(words=["abcd"], target="abcd"))
    print(s.numWays(words=["abab", "baba", "abba", "baab"], target="abba"))

    with open('number-of-ways-to-form-a-target-string-given-a-dictionary.input', 'r') as f:
        line = f.readline()
        line = line.replace('"', '')
        line = line.replace('[', '')
        line = line.replace(']', '')
        words = [x.strip() for x in line.split(',')]
        line = f.readline()
        line = line.replace('"', '')
        target = line.strip()
        t0 = time.time()
        print(s.numWays(words, target))
        print(time.time()-t0)
