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
        heads = [ListNode(float('-inf')) for _ in range(100)]
        for i in range(99):
            heads[i].up = heads[i+1]
            heads[i+1].down = heads[i]
        
        self.heads = heads
        self.height = 1
        
    def desc(self):
        print('#' * 80)
        for level in range(self.height-1, -1, -1):
            h = self.heads[level]
            q = []
            while h.next:
                q.append(h.next.val)
                h = h.next
            print('level {} {}'.format(level, q))

    def search(self, target: int) -> bool:
        h = self.heads[self.height - 1]
        while h:
            if h.val == target:
                return True
            if not h.next or h.next.val > target:
                h = h.down
            else:
                h = h.next
        
        return h is not None and h.val == target

    def add(self, num: int) -> None:
        curheight = 1
        while random.randint(1, 10) > 5:
            curheight += 1
        
        nodes = [ListNode(num) for _ in range(curheight)]
        for i in range(curheight-1):
            nodes[i].up = nodes[i+1]
            nodes[i+1].down = nodes[i]
        
        self.height = max(self.height, curheight)
        
        h = self.heads[self.height - 1]
        level = self.height - 1
        while h:
            while h.next and h.next.val < num:
                h = h.next
            
            if level < curheight:
                nxt = h.next
                node = nodes[level]
                h.next = node
                node.pre = h
                node.next = nxt
                if nxt:
                    nxt.pre = node
            
            level -= 1
            h = h.down

    def erase(self, num: int) -> bool:
        if not self.search(num):
            return False
        
        head = self.heads[self.height - 1]
        while head:
            if head.val == num:
                break
            if not head.next or head.next.val > num:
                head = head.down
            else:
                head = head.next
        while head.up:
            head = head.up
            
        while head:
            pre = head.pre
            nxt = head.next
            pre.next = nxt
            if nxt:
                nxt.pre = pre
            head.pre = None
            head.next = None
            head = head.down
            
        return True

        
if __name__ == '__main__':
    
    s = Skiplist()
    
    for op, param in zip(["Skiplist","add","add","add","search","add","search","erase","erase","search"], [[],[1],[2],[3],[0],[4],[1],[0],[1],[1]]):
        if op == "Skiplist":
            s = Skiplist()
        elif op == 'add':
            s.add(param[0])
        elif op == 'search':
            print(op, param, s.search(param[0]))
        else:
            print(op, param, s.erase(param[0]))
        
        # s.desc()
    
    
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