# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/8/25 10:33

"""

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tbyname = collections.defaultdict(list)

        ans = []
        transactions = [t.split(',') for t in transactions]
        transactions = [(t[0], int(t[1]), int(t[2]), t[3]) for t in transactions]
        for n, t, a, c in transactions:
            tbyname[n].append((n, t, a, c))

        for name, trans in tbyname.items():
            for t in trans:
                if t[2] > 1000:
                    ans.append(t)
                else:
                    if any([t2 != t and abs(t2[1]-t[1]) <= 60 and t2[3] != t[3] for t2 in trans]):
                        ans.append(t)
        return [','.join(t) for t in ans]


s = Solution()
print(s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]))
print(s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]))
print(s.invalidTransactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]))