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

# !/bin/python3

import math
import os
import random
import re
import sys

# !/bin/python3

import math
import os
import random
import re
import sys
import collections

if __name__ == '__main__':
    dp = [[-1 for _ in range(300005)] for _ in range(25)]
    
    
    
    def cnt(d, s):
        if d == -1 and s == 0:
            return 1
        elif d == -1:
            return 0
        elif dp[d][s] == -1:
            dp[d][s] = 0
            i = 0
            while i < 10 and (1 << d) * i <= s:
                dp[d][s] += cnt(d-1, s-(1 << d) * i)
                i += 1
        return dp[d][s]
        
    nm = [cnt(24, i) for i in range(300005)]
    for i in range(1, 300005):
        nm[i] += nm[i-1]
    
    N = int(input())
    for _ in range(N):
        x = int(input())
        if x == 1:
            print(0)
        else:
            ans = -1
            lo, hi = 0, 300004
            while lo <= hi:
                mid = (lo + hi) // 2
                if nm[mid] >= x:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            g = x - nm[ans-1]
            s = ans
            val = 0
            d = 0
            i = -1
            while cnt(i, s) < g:
                d = i
                i += 1
            
            d += 1
            while d >= 0:
                val = 0
                for i in range(10):
                    if s - (1 << d) * i >= 0:
                        val += cnt(d-1, s-(1<<d)*i)
                        
                    if val >= g:
                        print(i, end='')
                        g -= val - cnt(d - 1, s - (1 << d) * i)
                        s -= (1 << d) * i
                        break
                d -= 1
            print()