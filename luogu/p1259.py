# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/8/12 18:40

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List


if __name__ == '__main__':
    N = int(input())

    s = ['o'] * N + ['*'] * N + ['-'] * 2

    def dfs(index, s):
        if index <= 9:
            t = ''.join(s[10:])
            print('oooo****--' + t)
            print('ooo--***o*' + t)
            print('ooo*o**--*' + t)
            print('o--*o**oo*' + t)
            print('o*o*o*--o*' + t)
            print('--o*o*o*o*' + t)
            return

        print(''.join(s))
        for i in range(index):
            if s[i] == 'o' and s[i+1] == '*':
                s[index-1], s[index] = s[i], s[i+1]
                s[i], s[i+1] = '-', '-'
                print(''.join(s))
                s[i], s[i+1] = s[index-3], s[index-2]
                s[index-3], s[index-2] = '-', '-'
                # print(''.join(s))
                dfs(index-2, s)
                break

    dfs(len(s)-1, s)




