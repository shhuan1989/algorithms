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
created by shhuan at 2019/12/14 23:49

"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None
        self.up = None
        self.pre = None


class Skiplist:
    def __init__(self):
        self.head = ListNode(float('-inf'))

    def desc(self):
        print('=' * 40)
        h = self.head
        levels = 1
        while h.down:
            h = h.down
            levels += 1

        lastLevel = []
        hn = h
        while hn:
            lastLevel.append(hn.val)
            hn = hn.next

        ans = [[-1 for _ in range(len(lastLevel))] for _ in range(levels)]
        ans[-1] = lastLevel
        hn = h
        col = 0
        while hn:
            up = hn.up
            row = levels-2
            while up:
                ans[row][col] = up.val
                up = up.up
                row -= 1
            col += 1
            hn = hn.next

        for row in ans:
            print(' '.join(['-' if v == -1 else ('H' if v < 0 else str(v)) for v in row]))



    def search(self, target: int) -> bool:
        h = self.head
        while h:
            while h.next and h.next.val <= target:
                h = h.next
            if h.val == target:
                return True
            h = h.down
        return False

    def add(self, num: int) -> None:
        # print('add {}'.format(num))
        if self.search(num):
            return

        h = self.head
        while True:
            while h.next and h.next.val < num:
                h = h.next
            if h.down:
                h = h.down
            else:
                break
        while h.down:
            h = h.down

        newnode = ListNode(num)
        hnext = h.next
        h.next = newnode
        newnode.pre = h
        if hnext:
            newnode.next = hnext
            hnext.pre = newnode

        hpre = h
        cup = h.up
        while cup is None:
            hpre = hpre.pre
            if not hpre:
                break
            cup = hpre.up

        while cup and random.randint(1, 10) <= 5:
            upnode = ListNode(num)
            newnode.up = upnode
            upnode.down = newnode

            upnext = cup.next
            cup.next = upnode
            upnode.pre = cup
            if upnext:
                upnode.next = upnext
                upnext.pre = upnode

            newup = cup.up
            cpre = cup
            while newup is None:
                cpre = cpre.pre
                if not cpre:
                    break
                newup = cpre.up
            cup = newup
            newnode = upnode

        if not cup and random.randint(1, 10) <= 5:
            h = self.head
            newhead = ListNode(self.head.val)
            self.head = newhead
            newhead.down = h
            h.up = newhead

            upnode = ListNode(num)
            upnode.down = newnode
            newnode.up = upnode
            newhead.next = upnode
            upnode.pre = newhead

        self.desc()

    def erase(self, num: int) -> bool:
        # print('remove {}'.format(num))
        h = self.head
        while h:
            while h.next and h.next.val <= num:
                h = h.next
            if h.val == num:
                while h:
                    hpre, hnext, hdown = h.pre, h.next, h.down
                    h.pre = None
                    h.next = None
                    h.up = None
                    h.down = None
                    hpre.next = hnext
                    if hnext:
                        hnext.pre = hpre
                    if hdown:
                        hdown.up = None
                    h = hdown
                self.desc()
                return True
            h = h.down
        return False

s = Skiplist()

for i in range(50):
    if random.randint(1, 10) > 8:
        s.erase(random.randint(1, 10))
    else:
        s.add(random.randint(1, 10))


# a = ["Skiplist","add","add","add","add","add","add","add","add","add","erase","search","add","erase","erase","erase","add","search","search","search","erase","search","add","add","add","erase","search","add","search","erase","search","search","erase","erase","add","erase","search","erase","erase","search","add","add","erase","erase","erase","add","erase","add","erase","erase","add","add","add","search","search","add","erase","search","add","add","search","add","search","erase","erase","search","search","erase","search","add","erase","search","erase","search","erase","erase","search","search","add","add","add","add","search","search","search","search","search","search","search","search","search"]
# b = [[1],[16],[5],[14],[13],[0],[3],[12],[9],[12],[3],[6],[7],[0],[1],[10],[5],[12],[7],[16],[7],[0],[9],[16],[3],[2],[17],[2],[17],[0],[9],[14],[1],[6],[1],[16],[9],[10],[9],[2],[3],[16],[15],[12],[7],[4],[3],[2],[1],[14],[13],[12],[3],[6],[17],[2],[3],[14],[11],[0],[13],[2],[1],[10],[17],[0],[5],[8],[9],[8],[11],[10],[11],[10],[9],[8],[15],[14],[1],[6],[17],[16],[13],[4],[5],[4],[17],[16],[7],[14],[1]]
# for x, y in zip(a, b):
#     print(x, y[0])
# print('=' * 30)
# for x, y in zip(a, b):
#     if x == 'add':
#         s.add(y[0])
#     elif x == 'search':
#         print(s.search(y[0]))
#     elif x == 'erase':
#         print(s.erase(y[0]))

# [null,null,null,null,null,null,null,null,null,null,true,false,null,true,false,false,null,true,true,true,true,false,null,null,null,false,false,null,false,false,true,true,false,false,null,true,true,false,true,true,null,null,false,true,false,null,true,null,true,true,null,null,null,false,false,null,true,false,null,null,true,null,false,false,false,true,true,false,false,null,true,false,false,false,false,true,false,false,null,null,null,null,true,true,true,true,true,true,false,false,true]
# [null,null,null,null,null,null,null,null,null,null,true,false,null,true,false,false,null,true,true,true,true,false,null,null,null,false,false,null,false,false,true,true,false,false,null,true,true,false,true,true,null,null,false,true,false,null,true,null,true,true,null,null,null,false,false,null,true,false,null,null,true,null,false,false,false,true,true,false,true,null,true,false,false,false,true,true,false,false,null,null,null,null,true,true,true,true,true,true,false,false,true]