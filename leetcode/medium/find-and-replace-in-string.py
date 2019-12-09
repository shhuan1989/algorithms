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
created by shhuan at 2019/12/7 22:59

"""



s = Solution()
print(s.findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]))
print(s.findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]))
print(s.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]))
