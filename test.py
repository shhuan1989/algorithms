#!/bin/python

import math
import os
import random
import re
import sys




with open('/Users/shuangquan.huang/Downloads/videos.txt') as f1:
    a = [x.strip() for x in f1]
    
    with open('/Users/shuangquan.huang/Downloads/k4url.txt') as f2:
        b = [x.strip() for x in f2]
        # print(a[0])
        # print(b)
        
        ans = []
        for x in b:
            # print(x)
            if any([y.find(x) >= 0 for y in a]):
                continue
            ans.append(x)
        
        print('\n'.join(ans))
