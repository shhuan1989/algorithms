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
created by shhuan at 2019/12/4 23:46

"""
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [[t[0], int(t[1]), int(t[2]), t[3]] for t in [t.split(',') for t in transactions]]
        ans = []
        tbyname = collections.defaultdict(list)
        for t in transactions:
            tbyname[t[0]].append((t[1:]))

        for name, vals in tbyname.items():
            vals.sort()
            invalid = set()
            for i in range(len(vals)):
                a = vals[i]
                if a[1] > 1000:
                    invalid.add(i)
                for j in range(i+1, len(vals)):
                    b = vals[j]
                    if b[0] - a[0] > 60:
                        break
                    elif a[2] != b[2]:
                        invalid.add(i)
                        invalid.add(j)
            ans.extend([name] + vals[i] for i in invalid)

        return [','.join(map(str, v)) for v in ans]

s = Solution()
print(s.invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))
print(s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]))
print(s.invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]))
print(s.invalidTransactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]))
