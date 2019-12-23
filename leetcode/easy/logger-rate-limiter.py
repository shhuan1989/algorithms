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
created by shhuan at 2019/12/22 11:56

"""


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.printed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        self.printed = {k: v for k, v in self.printed.items() if v > timestamp - 10}

        if message not in self.printed:
            self.printed[message] = timestamp
            return True

        else:
            t = self.printed[message]
            if t > timestamp - 10:
                return False
            self.printed[message] = timestamp
            return True

logger = Logger()
print(logger.shouldPrintMessage(1, 'foo'))
print(logger.shouldPrintMessage(2, 'bar'))
print(logger.shouldPrintMessage(3, 'foo'))
print(logger.shouldPrintMessage(8, 'bar'))
print(logger.shouldPrintMessage(10, 'foo'))
print(logger.shouldPrintMessage(11, 'foo'))