# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/25/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
from functools import lru_cache

# TLE at the 91th test case, 97 cases in total
def solve_hash(s):
    MOD = 10**9+7
    N = len(s)
    ha, hb = 0, 0
    possible = []
    x, oa = 1, ord('a')
    w = [ord(v)-oa for v in s]
    for i, v in enumerate(w):
        ha = (ha * 26 + v) % MOD
        hb = (w[N-i-1] * x + hb) % MOD
        x = (x * 26) % MOD
        if ha == hb:
            possible.append((i+1))
    
    def check(m):
        l = possible[m]
        t = s.find(s[:l], 1)
        return t > 0 and t != N-l

    lo, hi = 0, len(possible)
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            lo = m + 1
        else:
            hi = m - 1
    
    return s[:possible[hi]] if hi >= 0 else 'Just a legend'
    
    
def solve_zscore(s):
    """
    https://cp-algorithms.com/string/z-function.html
    
    In z-function, z[i] means from i, the maximum number of chars is prefix of s.
    when i + z[i] == len(s), mean s[i:] == s[:z[i]], if there is another index j < i and z[j] >= z[i] means s[:z[i]]
    are prefix, suffix and another substring
    
    """
    z, maxl = [0] * len(s), 0
    i, l, r, n = 1, 0, 0, len(s)
    while i < n:
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        
        while i + z[i] < n and s[z[i]] == s[z[i] + i]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
        
        if i + z[i] == n:
            if z[i] <= maxl:
                return s[:z[i]]
        maxl = max(maxl, z[i])
        i += 1
        
    return 'Just a legend'


def solve_prefix(s):
    """
    https://cp-algorithms.com/string/prefix-function.html
    The prefix function for this string is defined as an array π of length n,
    where π[i] is the length of the longest proper prefix of the substring s[0…i]
    which is also a suffix of this substring.
    A proper prefix of a string is a prefix that is not equal to the string itself. By definition, π[0]=0.
    """
    n, pi = len(s), [0] * len(s)
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    
    if pi[-1] > 0:
        if any([pi[i] >= pi[-1] for i in range(n - 1)]):
            return s[:pi[-1]]
        else:
            p = pi[pi[-1] - 1]
            if p > 0:
                return s[:p]
    return 'Just a legend'
    
    
s = input()
# solve_zscore(s)
print(solve_prefix(s))