# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/7/31

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

if __name__ == '__main__':
    N = int(input())
    text = input().strip()
    words = []
    for i in range(N):
        words.append(input().strip())
        
    trie = {}
    for word in words:
        t = trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
        t['#'] = True
    
    wmap = {
        '1': 'abc',
        '2': 'def',
        '3': 'ghi',
        '4': 'jkl',
        '5': 'mn',
        '6': 'opq',
        '7': 'rst',
        '8': 'uvw',
        '9': 'xyz',
    }
    
    ntext = len(text)
    q = [(0, trie, [''])]
    while q:
        index, t, pre = q.pop()
        if index >= ntext:
            if '#' in t:
                print(' '.join(pre).strip(), end='')
                exit(0)
        else:
            if '#' in t:
                q.append((index, trie, pre + ['']))
            
            for ch in wmap[text[index]]:
                if ch not in t:
                    continue
                q.append((index + 1, t[ch], pre[:-1] + [pre[-1] + ch]))
            
    print('No Solutions!')
    
        
        
            