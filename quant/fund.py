# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/11/10

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

import requests
import pandas as pd
from operator import itemgetter
from tqdm import tqdm
from bs4 import BeautifulSoup
import numpy as np

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
        with open(self.map_file, 'wb') as f:
            pickle.dump(self.cache_map, f)
        f.close()


def getfundprofit(code, start, end):
    params = {
        # 'callback': 'setListData',
        'symbol': code,
        'firstday': start,
        'endday': end,
        'day': 'd01',
        'dtnum': 500,
        'purate': 0.015,
        'dpc': 1
    }
    url = 'https://stock.finance.sina.com.cn/fundfilter/api/openapi.php/DingtouFundFilterService.getDingTouProfit'
    r = requests.get(url, params)

    d = r.json()['result']['data'][0]
    print(d)
    if int(d['dtmoney']) > 0:
        return (float(d['summoney']), float(d['dtprofit']), float(d['profitrate'][:-1]))
    else:
        return None
        

def getfundlist() -> pd.DataFrame:
    dest = './data/fundlist.csv'
    if os.path.exists(dest):
        df = pd.read_csv(dest, index_col=0)
        return df
    
    params = {
        'page_size': 20,
    }
    url = 'http://fund.sina.com.cn/fund/api/fundMarketList'
    
    pagecount = 171
    for page in tqdm(range(1, pagecount)):
        path = './data/tmp/codes_{}.csv'.format(page)
        
        params['page_no'] = page
        
        while not os.path.exists(path):
            try:
                resp = requests.get(url, params)
                data = resp.json()['data']['items']
                
                df = pd.DataFrame(data)
                # print(df.head())
                df.to_csv(path, index=False)
            except Exception as e:
                print(e)
        
    
    df = pd.DataFrame()
    for page in range(1, pagecount):
        path = './data/tmp/codes_{}.csv'.format(page)
        cdf = pd.read_csv(path, index_col=0)
        if df.empty:
            df = cdf
        else:
            df = df.append(cdf)
    # print(df.describe())
    
    df = df.sort_values(by=['id'])
    
    df.to_csv(dest)
    
    return df


def fetchurl(url):
    path = '.data/cache/'

def get_manager_avg_gain(url):
    print(url)
    h = HttpGetter()
    text = h.get(url)
    soup = BeautifulSoup(text, 'html5lib')
    gain = []
    for x in soup.select('#middle > div.blk02 > table:nth-child(6) > tbody > tr > td:nth-child(5)')[1:]:
        try:
            gain.append(float(x.string[:-1]))
        except:
            pass
    
    # print(gain)
    avggain = np.average(gain)
    return avggain

def get_manager_info(url):
    print(url)
    h = HttpGetter()
    text = h.get(url)
    h.close()
    with open('./data/manager/{}.html'.format(url[url.find('mid=')+4:]), 'w') as f:
        f.write(text)
    


if __name__ == '__main__':
    
    # df = getfundlist()
    # print(len(df))
    # print(df.columns)
    # print(df.describe())
    #
    # df = df.sort_values(by=['three_year_incratio', 'year_incratio'])
    # print(df[:100])
    
    top_manager = pd.read_csv('./data/topmanager.csv')
    for url in top_manager[['url']].values.flatten().tolist():
        get_manager_info(url)
    # top_manager['avg_profit'] = top_manager.apply(lambda row: get_manager_avg_gain(row['url']), axis=1)
    # print(top_manager)
    # top_manager.to_csv('./data/topmanager.csv')
    
    
    