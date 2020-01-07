# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/29 10:41

"""


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if any([len(w) > len(result) for w in words]):
            return False

        chs = set()
        for w in words:
            chs |= set(w)
        chs |= set(result)
        if len(chs) > 10:
            return False

        chs = list(sorted(chs))
        num = [0 for _ in range(len(chs) + 1)]
        chi = {v: i for i, v in enumerate(chs)}
        chi[' '] = len(chs)
        first = [False for _ in range(len(chs))]
        for ch in {w[0] for w in words} | {result[0]}:
            first[chi[ch]] = True

        N = len(result)
        words = [' ' * (N-len(w)) + w for w in words]


        def dfs(index, cap, rest, used):
            if index < 0:
                print(num)
                print(chi)
                return True

            adds = {w[index] for w in words} | {result[index]}
            adds -= used
            adds -= {' '}
            adds = list(adds)
            if index == 0:
                rest -= {0}

            for perm in itertools.permutations(rest, len(adds)):
                for u, v in zip(adds, perm):
                    num[chi[u]] = v
                s = sum([num[chi[w[index]]] for w in words]) + cap
                t = num[chi[result[index]]]

                if s % 10 == t and dfs(index-1, s // 10, rest - set(perm), used | set(adds)):
                    return True

            return False

        return dfs(N-1, 0, {i for i in range(10)}, set())






s = Solution()
print(s.isSolvable(["TO","BE","OR","NOT"], "TOBE"))
# print(s.isSolvable(words = ["SEND","MORE"], result = "MONEY"))
# print(s.isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"))
# print(s.isSolvable(words = ["THIS","IS","TOO"], result = "FUNNY"))
# print(s.isSolvable(words = ["LEET","CODE"], result = "POINT"))
