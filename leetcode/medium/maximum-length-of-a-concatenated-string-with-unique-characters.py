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
created by shhuan at 2019/12/18 23:27

"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        N, A = len(arr), arr

        def dfs(pre, index):
            if len(set(pre)) != len(pre):
                return 0

            if index >= N:
                return len(pre)

            return max(dfs(pre + A[index], index+1), dfs(pre, index+1))

        return dfs('', 0)