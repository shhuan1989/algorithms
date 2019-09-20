# -*- coding: utf-8 -*-

"""
created by shhuan at 2019/9/13 23:25

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
    def maxRepOpt1(self, text: str) -> int:
        if not text:
            return 0

        n = len(text)
        if len(set(text)) == 1:
            return n

        q = collections.defaultdict(list)
        l, r, ans = 0, 0, 0

        while r < n:
            if text[r] != text[l]:
                q[text[l]].append((l, r))
                l = r
            r += 1
        q[text[l]].append((l, n))

        ans = max([max([v[1]-v[0] for v in u]) for u in q.values()])

        wc = collections.Counter(text)
        o1 = len(wc.keys()) == 2 and min(wc.values()) == 1

        # print(q)
        for u in q.values():
            for i in range(len(u)-1):
                if u[i][1] == u[i+1][0] - 1:
                    ans = max(ans, u[i+1][1] - u[i][0] -(1 if o1 else 0))

        ans = max(ans, max([max([min(v[1]-v[0]+1, wc[k]) for v in u]) for k, u in q.items()]))


        return ans


s = Solution()
print(s.maxRepOpt1('ababa'))
print(s.maxRepOpt1('aaabaaa'))
print(s.maxRepOpt1('aaabbaaa'))
print(s.maxRepOpt1('aaaaa'))
print(s.maxRepOpt1('abcdef'))
print(s.maxRepOpt1('aabbabaaaabaabaabaaaaaababbbabaaabbaabbbaaababbbaaaababaabbabaaabbbaaaababaabbbabaababbaabaaababbabbabaabbabaaabbbbabaabaabbbaabaaabbbbbaababaabbbabbbbaababbaaaaaabbbbbbaaaabbaaaabaabbabbabbbaabababbbbabaabaabaabbabbbbbbbaaababaaaabbbbaaababaaabbbbabaabbabaabbbbbbbaaabbbabaaababaababaabaababbabbbbabbabaaabaabaaaabbabbbaabaaabababaaabbbababaaabbabbaaabbbbbaabbbabbbabaabababbaabaaaabbabaaabbaababaabbbaabbbababbbbbabbaabbaabbbbbbabababbabaaaabbaabbbbbbabbabbabababaababaaabaaaababbbbbaaabbbabaaaababaaabbbbaaaabbbabbaaababbbabbaaabbaaaaabbbbabbbababbbabbbaaabaabbbbbababbaabbbaabbabaabaaaaabbbabbbbbbabbbbbbababaaabbbabbbaabbbbabbaaababababbabaaaaabaaababaaababbbbbabaababbbbbbbbaaaaabbabbabbabbbabbaabbaaabbabbaaabbbabaaaabbaaababbbbbbbaabbabbbabbbbbbaabababbbbaaaabbbaaababbaabaababaaababbabbabbabbabbbbbabaaaaabababbaabababbabaabbaabbbbbabbbabaaaabbbbaaaabbbbaababbabbbbaababaaabbaaaabbbbababaaabbabbbaababbbaaabbaabbbbbbbbbabbbababbaabbaaabbbaaaaabbbbabaaaaaaabaaabaaabbbbabaaaabbaaaabaaabbbbaa'))