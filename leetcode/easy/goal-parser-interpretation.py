# -*- coding: utf-8 -*-

"""
created by shhuan at 2020/12/6 10:30

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


class Solution:
    def interpret(self, command: str) -> str:
        if not command:
            return None

        command = command.replace('()', 'o')
        command = command.replace('(al)', 'al')

        return command


if __name__ == '__main__':
    s = Solution()
    print(s.interpret('G()(al)'))
    print(s.interpret('G()()()()(al)'))
    print(s.interpret('(al)G(al)()()G'))
