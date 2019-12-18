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
created by shhuan at 2019/12/19 00:26

"""


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:
            return False
        N = len(words)
        for r in range(N):
            row = words[r]
            L = len(row)
            col = ''
            for nr in range(N):
                if len(words[nr]) <= r:
                    col += ' '
                else:
                    col += words[nr][r]
            if row != col[: L] or any([ch != ' ' for ch in col[L: ]]):
                return False

        return True

s = Solution()
print(s.validWordSquare(["abcd","bnrt","crm","dt"]))
print(s.validWordSquare([
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
))
print(s.validWordSquare(
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]
))
print(s.validWordSquare(
[
  "ball",
  "area",
  "read",
  "lady"
]
))