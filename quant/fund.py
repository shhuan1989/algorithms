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
import json

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
            f = open(self.map_file, 'rb')
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
    
    gain = get_manager_gains(url)
    # print(gain)
    avggain = np.average(gain)
    return avggain

def get_manager_gain_std(url):
    gain = get_manager_gains(url)
    return np.std(gain)

def get_manager_gain_str(url):
    gain = get_manager_gains(url)
    return ','.join(map(str, gain))
    

def get_manager_gains(url):
    print(url)
    h = HttpGetter()
    text = h.get(url)
    h.close()
    soup = BeautifulSoup(text, 'html5lib')
    gain = []
    for x in soup.select('#middle > div.blk02 > table:nth-child(6) > tbody > tr > td:nth-child(5)')[1:]:
        try:
            gain.append(float(x.string[:-1]))
        except:
            pass
    return gain
    

def get_manager_info(url):
    print(url)
    h = HttpGetter()
    text = h.get(url)
    h.close()
    
    soup = BeautifulSoup(text, 'html5lib')
    starttime = soup.select('#middle > div.blk02 > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)')[0].string
    education = soup.select('#middle > div.blk02 > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(6)')[0].string
    
    return {
        'start_time': starttime,
        'education': education,
    }
    
    

def get_top_manager(percent, cache=True):
    path = './data/top_{}.csv'.format(percent)
    managerpath = './data/topmanager_{}.csv'.format(percent)
    
    if os.path.exists(managerpath) and cache:
        df = pd.read_csv(managerpath)
        return df
    
    df = getfundlist()
    # print(len(df))
    # print(df.columns)
    # print(df.describe())
    
    size = len(df) * percent // 100
    
    print(size)
    top10in3y = df.sort_values(by=['three_year_incratio'], ascending=False)[:size]
    top10in1y = df.sort_values(by=['year_incratio'], ascending=False)[:size]
    
    codesinboth = set(top10in3y[['fund_code']].values.flatten().tolist())
    codesinboth = codesinboth.intersection(set(top10in1y[['fund_code']].values.flatten().tolist()))
    codesinboth = list(codesinboth)
    
    top10 = df[df['fund_code'].isin(codesinboth)]
    
    top10.to_csv(path)
    
    managers_col = top10[['fund_manager']].dropna().values.tolist()
    
    # print(managers[:2])
    managers = {}
    for x in managers_col:
        y = json.loads(x[0].replace('\'', '\"'))
        # print(x[0])
        for z in y:
            managers[z['name']] = z['url']
    
    managers = [(k, v) for k, v in managers.items()]
    mdf = pd.DataFrame(managers, columns=['name', 'url'])
    
    mdf['avg_profit'] = mdf.apply(lambda row: get_manager_avg_gain(row['url']), axis=1)
    mdf['profit_std'] = mdf.apply(lambda row: get_manager_gain_std(row['url']), axis=1)
    mdf['profits'] = mdf.apply(lambda row: get_manager_gain_str(row['url']), axis=1)
    mdf = mdf.sort_values(by=['avg_profit'], ascending=False)
    mdf.to_csv(managerpath, index=False)
    
    return mdf
    


if __name__ == '__main__':
    
    # print(get_manager_info('http://stock.finance.sina.com.cn/manager/view/mInfo.php?mid=30189744'))
    
    df = get_top_manager(10, cache=True)
    
    over5 = []
    for _, row in df.iterrows():
        info = get_manager_info(row['url'])
        print(row['name'], info)
        
        year = info['start_time']
        if int(year[:year.find('年')]) > 4:
            over5.append(row.values.flatten().tolist() + [info['start_time'], info['education']])
    
    df2 = pd.DataFrame(data=over5, columns=df.columns.tolist() + ['time', 'education'])
    print(df2.head(10))
    
    df2.to_csv('top10_over_5year.csv')
    # print(over5)
        # print(row)
    
    
    # print(df[['name', 'avg_profit', 'profit_std']].head(10))
    # managers = df.values.tolist()
    # print(managers[:10])
    
    
    