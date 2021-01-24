# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/13 10:32

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
    def minPartitions(self, n: str) -> int:
        return max([int(x) for x in n])


if __name__ == '__main__':
    s = Solution()
    print(s.minPartitions('32'))
    print(s.minPartitions('82734'))
    print(s.minPartitions('27346209830709182346'))