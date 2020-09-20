import math
import os
import random
import re
import sys
from typing import List
import bisect
import collections
import heapq

import numpy as np



class Bundle:
    def __init__(self, size, count, price):
        self.size = size
        self.count = count
        self.price = price

    def __cmp__(self, other):
        return self.size - other.size


if __name__ == '__main__':

    area = [(200, 500), (250, 90), (120, 90)]

    bundles = [Bundle(60, 4, 49.0), Bundle(30, 9, 18.5)]

    def up(a, b):
        return a // b if a % b == 0 else a // b + 1

    def dfs(index, pre, precost, area):
        w, h = area
        b = bundles[index]

        print(precost, pre, area)

        if index >= len(bundles) - 1:
            count = up(up(w, b.size) * up(h, b.size), b.count)
            return precost + count * b.price, pre + [(index, count)]



        count = up(up(w, b.size) * up(h, b.size), b.count)
        mincost = float('inf')
        buy = []

        for i in range(count+1):
            cost, cb = dfs(index+1, pre + [(index, i)], precost + i * b.price, (w, h - i * b.count // up(w, b.size) * b.size))
            if cost < mincost:
                mincost = cost
                buy = cb

        return mincost, buy


    print(dfs(0, [], 0, (200, 500)))