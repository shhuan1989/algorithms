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
created by shhuan at 2019/12/10 20:24

"""

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def match(word):
            wi = 0
            for p in pattern:
                while wi < len(word):
                    if word[wi] == p:
                        break
                    elif word[wi].isupper():
                        return False
                    else:
                        wi += 1
                if wi >= len(word):
                    return False
                if word[wi] == p:
                    wi += 1

            return all([w.islower() for w in word[wi:]])

        def match2(word):
            for p in pattern:
                i = word.find(p)
                if i < 0 or i >= len(word):
                    return False
                if any([w.isupper() for w in word[:i]]):
                    return False
                word = word[i+1:]

            return all([w.islower() for w in word])

        return [match(word) for word in queries]


s = Solution()
print(s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"))
print(s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"))
print(s.camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"))