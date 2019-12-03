import math
import os
import random
import re
import sys
<<<<<<< Updated upstream
=======

from typing import List
import bisect

import collections
from functools import cmp_to_key



class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = []
        self.subCount = 0
        self.pCount = 0
        self.unpub = 0
        self.own = 0
        self.total = 0

class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:

        team = [Node(i) for i in range(n+1)]
        MOD = 1000000007

        for a, b in leadership:
            team[b].parent = team[a]
            team[a].children.append(team[b])

        for i in range(1, n+1):
            m = team[i]
            pCount = 0
            while m.parent:
                m.parent.subCount += 1
                m = m.parent
                pCount += 1
            team[i].pCount = pCount

        ans = []
        for v in operations:
            a, b = v[0], v[1]
            m = team[b]
            if a == 1:
                m.own += v[2]
                m.own %= MOD
                # while m.parent:
                #     m.parent.total += v[2]
                #     m.parent.total %= MOD
                #     m = m.parent
            elif a == 2:
                m.unpub += v[2]
                m.unpub %= MOD
                # while m.parent:
                #     m.parent.total += v[2] * (team[b].subCount+1)
                #     m.parent.total %= MOD
                #     m = m.parent
            else:
                count = m.own + m.unpub * m.subCount
                while m.parent:
                    p = m.parent
                    if p.unpub > 0:
                        for c in p.children:
                            c.unpub += p.unpub
                        count += p.unpub
                        count %= MOD
                        p.unpub = 0
                    m = p

                while m.children

                ans.append(count%MOD)

        return ans




s = Solution()
print(s.bonus(n = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]))
>>>>>>> Stashed changes
