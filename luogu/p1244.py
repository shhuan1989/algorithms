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
created by shhuan at 2020/7/28 18:21

"""


if __name__ == '__main__':
    H, K = map(int, input().strip().split())
    print(2**H * (K+1))