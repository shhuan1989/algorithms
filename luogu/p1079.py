# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


if __name__ == '__main__':
    
    R = []
    start = 0
    base = [i for i in range(26)]
    for i in range(26):
        row = base[start:] + base[:start]
        R.append(row)
        start += 1
        
    cipher = input().upper()
    encrypted = input()
    
    def getuncrypted(che, chc):
        islower = che.islower()
        che = che.upper()
        for i in range(26):
            if R[i][ord(chc)-ord('A')] == ord(che) - ord('A'):
                ch = chr(ord('A') + i)
                if islower:
                    return ch.lower()
                else:
                    return ch
    ans = ''
    ci = 0
    for i, v in enumerate(encrypted):
        ans += getuncrypted(v, cipher[ci])
        ci = (ci+1) % len(cipher)
    
    print(ans)
    
    
        