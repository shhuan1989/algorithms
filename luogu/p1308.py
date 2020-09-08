# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/7

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    # sys.stdin = open('P1308_1.in', 'r')
    pattern = input().strip().lower()
    text = input().lower()
    
    ans = -1
    i = 0
    words = collections.defaultdict(list)
    while i < len(text):
        if text[i] != ' ':
            r = i
            while r < len(text) and text[r] != ' ':
                r += 1
            words[text[i: r]].append(i)
            i = r
        else:
            i += 1
    
    # print(words)
    ans = len(words[pattern])
    if ans == 0:
        print(-1)
    else:
        print('{} {}'.format(ans, words[pattern][0]))