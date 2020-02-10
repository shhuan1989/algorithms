# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class TweetCounts(object):
    
    def __init__(self):
        self.data = collections.defaultdict(list)
    
    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        self.data[tweetName].append(time)
    
    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        
        a = [t for t in self.data[tweetName] if startTime <= t <= endTime]
        a.sort()
        
        ans = []
        i = 1
        d = 60 if freq == 'minute' else (3600 if freq == 'hour' else 60 * 60 * 24)
        c = 0
        for t in a:
            if t < startTime + i * d:
                c += 1
            else:
                i += 1
                ans.append(c)
                c = 1
        if c > 0:
            ans.append(c)
        return ans
        
        

s = TweetCounts()
s.recordTweet('t3', 0)
s.recordTweet('t3', 60)
s.recordTweet('t3', 10)
print(s.getTweetCountsPerFrequency('minute', 't3', 0, 59))
print(s.getTweetCountsPerFrequency('minute', 't3', 0, 60))
s.recordTweet('t3', 120)
print(s.getTweetCountsPerFrequency('hour', 't3', 0, 210))