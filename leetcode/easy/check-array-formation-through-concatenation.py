# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/11/1 10:30

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
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        def flatten(a):
            if type(a) == int:
                return [a]
            ret = []
            for v in a:
                ret += flatten(v)

            return ret

        fp = flatten(pieces)
        if len(arr) != len(fp) or list(sorted(arr)) != list(sorted(fp)):
            return False


        i = 0
        np = len(pieces)
        pieces = [flatten(v) for v in pieces]
        used = [False for _ in range(np)]
        while i < len(arr):
            find = False
            for j in range(np):
                if not used[j]:
                    if pieces[j][0] == arr[i]:
                        k = len(pieces[j])
                        if arr[i: i+k] != pieces[j]:
                            return False
                        i += k
                        used[j] = True
                        find = True
                        break
            if not find:
                return False

        return True



if __name__ == '__main__':
    s = Solution()
    print(s.canFormArray(arr = [85], pieces = [[85]]))
    print(s.canFormArray(arr = [15,88], pieces = [[88],[15]]))
    print(s.canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))
    print(s.canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))
    print(s.canFormArray(arr=[1, 3, 5, 7], pieces=[[2, 4, 6, 8]]))

