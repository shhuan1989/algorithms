# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/12

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

import pickle
import requests

class HttpGetter:
    def __init__(self):
        self.cache_folder = './data/cache'
        
        if not os.path.exists(self.cache_folder):
            os.makedirs(self.cache_folder)
        
        self.map_file = './data/cache/urlmap.pkl'
        if not os.path.exists(self.map_file):
            self.cache_map = {}
        else:
            f = open(self.map_file, 'r')
            self.cache_map = pickle.load(f)
            f.close()
        
    
    def get(self, url):
        cache = self.read_cache(url)
        if cache is not None:
            return cache
        
        
        path = './data/cache/{}.html'.format(time.time())
        self.cache_map[url] = path
        
        resp = requests.request('GET', url, timeout=10)
        text = resp.text
        
        with open(path, 'w') as f:
            f.write(text)
        
        f.close()
        
        return text
        
        
        
    def read_cache(self, url):
        if url not in self.cache_map:
            return None
        
        path = self.cache_map[url]
        f = open(path)
        text = '\n'.join(f.readlines())
        f.close()
        
        return text
    
    
    def close(self):
        with open(self.map_file, 'w') as f:
            pickle.dump(self.cache_map, f)
        f.close()