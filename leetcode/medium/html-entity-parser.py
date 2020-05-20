# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/4/13

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def entityParser(self, text: str) -> str:
        
        ans = []
        
        i = 0
        while i < len(text):
            if text[i] == '&':
                if text[i: i+6] == '&quot;':
                    ans.append('"')
                    i += 6
                elif text[i: i+ 6] == '&apos;':
                    ans.append('\'')
                    i += 6
                elif text[i: i+5] == '&amp;':
                    ans.append('&')
                    i += 5
                elif text[i: i+4] == '&gt;':
                    ans.append('>')
                    i += 4
                elif text[i: i+4] == '&lt;':
                    ans.append('<')
                    i += 4
                elif text[i: i+7] == '&frasl;':
                    ans.append('/')
                    i += 7
                else:
                    ans.append(text[i])
                    i += 1
            else:
                ans.append(text[i])
                i += 1
    
        return ''.join(ans)
    
s = Solution()
print(s.entityParser("&amp; is an HTML entity but &ambassador; is not."))
print(s.entityParser("&amp;gt;"))