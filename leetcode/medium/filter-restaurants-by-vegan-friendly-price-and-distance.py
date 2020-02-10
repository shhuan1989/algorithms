# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/26/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        restaurants = [v for i, v in enumerate(restaurants)]
        restaurants = [v for v in restaurants if v[3] <= maxPrice and v[4] <= maxDistance]
        if veganFriendly:
            restaurants = [v for v in restaurants if v[2] == 1]
            
        restaurants = [[v[1]] + v for i, v in enumerate(restaurants)]
        restaurants.sort(reverse=True)
        
        # print(restaurants)
        return [v[1] for v in restaurants]
    
    
s = Solution()
# print(s.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10))
# print(s.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10))
# print(s.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3))
print(s.filterRestaurants([[33433,15456,1,99741,58916],[61899,85406,1,27520,12303],[63945,3716,1,56724,79619]], 0, 91205, 58378))