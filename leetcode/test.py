# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/15 22:16

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def discount(val):
    if val >= 299:
        return val - 60
    if val >= 199:
        return val - 30

    return val

xy = [[109, 54], [215, 108], [128, 68]]

ans = []
for a in range(10):
    for b in range(10):
        for c in range(10):
            amounts = [a, b, c]
            cost = sum([amounts[i] * xy[i][0] for i in range(3)])
            amount = sum([amounts[i] * xy[i][1] for i in range(3)])
            if amount == 0 or amount > 300:
                continue

            dcost = discount(cost)
            avg = dcost / amount
            ans.append((avg, dcost, cost, amount, a, b, c))
ans.sort()
print(ans[:10])


print(discount(512))