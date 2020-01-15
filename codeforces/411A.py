# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/14/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def check(password):
    if len(password) < 5:
        return False
    
    hasUpper = any([v in [chr(ord('A')+i) for i in range(26)] for v in password])
    hasLower = any([v in [chr(ord('a')+i) for i in range(26)] for v in password])
    
    if not hasLower or not hasUpper:
        return False
    
    hasDigit = any([v in [str(i) for i in range(10)] for v in password])
    if not hasDigit:
        return False
    
    return True


password = input()
valid = check(password)
print('Correct' if valid else 'Too weak')