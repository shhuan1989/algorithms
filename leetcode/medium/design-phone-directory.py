# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/9/15

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.numbers = collections.deque([i for i in range(maxNumbers)])
        self.used = set()


    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if not self.numbers:
            return -1
        
        number = self.numbers.popleft()
        self.used.add(number)
        return number


    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number not in self.used


    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.used:
            self.used.discard(number)
            self.numbers.append(number)


if __name__ == '__main__':
    s = PhoneDirectory(0)
    for op, params in zip(["PhoneDirectory","release","get","release","release","get","get","check","get","release","get","release","release","get","check","release"], [[3],[2],[],[2],[0],[],[],[1],[],[0],[],[0],[0],[],[1],[1]]):
        if op == 'PhoneDirectory':
            s = PhoneDirectory(params[0])
        elif op == 'release':
            s.release(params[0])
        elif op == 'get':
            print(s.get())
        else:
            print(s.check(params[0]))

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
