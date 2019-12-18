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
created by shhuan at 2019/12/18 23:14

"""


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        dictionary = set(dictionary)
        w2a = {}
        a2w = {}
        used = set()
        dup = set()

        for w in dictionary:
            abbrev = w if len(w) <= 2 else '{}{}{}'.format(w[0], len(w) - 2, w[-1])
            w2a[w] = abbrev
            if abbrev in dup:
                continue
            if abbrev in used:
                dup.add(abbrev)
            else:
                used.add(abbrev)
                a2w[abbrev] = w

        self.dup = dup
        self.used = used
        self.a2w = a2w
        self.w2a = w2a


    def isUnique(self, word: str) -> bool:
        abbrev = word if len(word) <= 2 else '{}{}{}'.format(word[0], len(word)-2, word[-1])

        return abbrev not in self.used or (abbrev not in self.dup and self.a2w[abbrev] == word)

