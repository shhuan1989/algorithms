# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/9 10:30

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
    def makeGood(self, s: str) -> str:
        q = []
        for v in s:
            if v.isupper():
                if q and q[-1].islower() and q[-1].upper() == v:
                    q.pop()
                else:
                    q.append(v)
            else:
                if q and q[-1].isupper() and q[-1].lower() == v:
                    q.pop()
                else:
                    q.append(v)

        return ''.join(q)

if __name__ == '__main__':
    s = Solution()
    print(s.makeGood('leEeetcode'))
    print(s.makeGood('abBAcC'))
    print(s.makeGood('s'))
    print(s.makeGood('Pp'))