# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/16

"""

import collections
import time
import os
import sys
import bisect
import heapq
import itertools
from functools import lru_cache
from typing import List


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, nx: int, wx: int) -> int:
        # 如果 x 和 y 相邻，需要加上的分数
        def calc(x: int, y: int) -> int:
            if x == 0 or y == 0:
                return 0
            # 例如两个内向的人，每个人要 -30，一共 -60，下同
            if x == 1 and y == 1:
                return -60
            if x == 2 and y == 2:
                return 40
            return -10
        
        n3 = 3 ** n
        # 预处理：每一个 mask 的三进制表示
        mask_span = dict()
        # 预处理：每一个 mask 去除最高位、乘 3、加上新的最低位的结果
        truncate = dict()
        
        # 预处理
        highest = n3 // 3
        for mask in range(n3):
            mask_tmp = mask
            bits = list()
            for i in range(n):
                bits.append(mask_tmp % 3)
                mask_tmp //= 3
            # 与方法一不同的是，这里需要反过来存储，这样 [0] 对应最高位，[n-1] 对应最低位
            mask_span[mask] = bits[::-1]
            truncate[mask] = [
                mask % highest * 3,
                mask % highest * 3 + 1,
                mask % highest * 3 + 2,
            ]
        
        # dfs(位置，轮廓线上的 mask，剩余的内向人数，剩余的外向人数)
        @lru_cache(None)
        def dfs(pos: int, borderline: int, nx: int, wx: int):
            # 边界条件：如果已经处理完，或者没有人了
            if pos == m * n or nx + wx == 0:
                return 0
            
            x, y = divmod(pos, n)
            
            # 什么都不做
            best = dfs(pos + 1, truncate[borderline][0], nx, wx)
            # 放一个内向的人
            if nx > 0:
                best = max(best, 120 + calc(1, mask_span[borderline][0]) \
                           + (0 if y == 0 else calc(1, mask_span[borderline][n - 1])) \
                           + dfs(pos + 1, truncate[borderline][1], nx - 1, wx))
            # 放一个外向的人
            if wx > 0:
                best = max(best, 40 + calc(2, mask_span[borderline][0]) \
                           + (0 if y == 0 else calc(2, mask_span[borderline][n - 1])) \
                           + dfs(pos + 1, truncate[borderline][2], nx, wx - 1))
            
            return best
        
        return dfs(0, 0, nx, wx)
                            
                            
if __name__ == '__main__':
    s = Solution()
    print(s.getMaxGridHappiness(2, 3, 1, 2))
    print(s.getMaxGridHappiness(3, 1, 2, 1))
    print(s.getMaxGridHappiness(2, 2, 4, 0))
    print(s.getMaxGridHappiness(3, 1, 2, 1))