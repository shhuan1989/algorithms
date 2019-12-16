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
created by shhuan at 2019/12/12 20:50

"""

class Solution:
    def encode(self, s: str) -> str:

        dp = [[]]
